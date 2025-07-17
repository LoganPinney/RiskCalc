"""Minimalist Win95-style trading risk calculator."""

import PySimpleGUI as sg
import matplotlib
matplotlib.use('TkAgg')  # use TkAgg backend for PySimpleGUI
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def compute_trade_metrics(price, capital, stop_pct, risk_pct, target_ratio):
    """Compute risk metrics based on inputs."""
    try:
        price = float(price)
        capital = float(capital)
    except (ValueError, TypeError):
        return None
    stop_price = price * (1 - stop_pct / 100)
    risk_per_trade = capital * (risk_pct / 100)
    risk_per_share = price - stop_price
    shares = risk_per_trade / risk_per_share if risk_per_share > 0 else 0
    shares = int(shares)
    target_price = price + target_ratio * (price - stop_price)
    reward_per_share = target_price - price
    reward_per_trade = reward_per_share * shares
    rr_ratio = reward_per_share / risk_per_share if risk_per_share != 0 else 0
    return {
        "stop_price": stop_price,
        "target_price": target_price,
        "risk_per_trade": risk_per_trade,
        "reward_per_trade": reward_per_trade,
        "shares": shares,
        "rr_ratio": rr_ratio,
    }


def draw_chart(canvas, fig_agg, ax, price, stop_price, target_price):
    """Draw or update the matplotlib chart."""
    ax.cla()
    diff_stop = price - stop_price
    diff_target = target_price - price
    ax.bar(0, diff_target, width=0.5, bottom=0, color="green")
    ax.bar(0, -diff_stop, width=0.5, bottom=0, color="red")
    ax.scatter(0, diff_target, color="black")
    ax.scatter(0, -diff_stop, color="black")
    ax.axhline(0, color="blue", linestyle="--")
    ax.set_xticks([])
    ax.set_ylabel("Price Movement")
    ax.set_title("Risk / Reward Zones")
    ax.set_ylim(-diff_stop * 1.2 if diff_stop > 0 else -1, diff_target * 1.2 if diff_target > 0 else 1)
    fig_agg.draw()


def create_window():
    sg.theme("SystemDefault")
    sg.set_options(font=("MS Sans Serif", 10))
    input_col = [
        [sg.Text("Stock Price"), sg.Input(key="-PRICE-", size=(10,1), justification='right')],
        [sg.Text("Capital Available"), sg.Input(key="-CAPITAL-", size=(10,1), justification='right')],
        [sg.Text("Stop-Loss %"), sg.Slider(range=(0.5,10), default_value=1.0, resolution=0.1,
                                           orientation='h', key="-STOP-")],
        [sg.Text("Risk per Trade %"), sg.Slider(range=(0.5,10), default_value=1.0, resolution=0.1,
                                               orientation='h', key="-RISK-")],
        [sg.Text("Target P&L Ratio"), sg.Slider(range=(0,10.0), default_value=2.0, resolution=0.1,
                                             orientation='h', key="-RATIO-")],
        [sg.Frame("Results", [
            [sg.Text("Stop-Loss Price", size=(18,1)), sg.Text("", key="-STOPPRICE-")],
            [sg.Text("Profit Target", size=(18,1)), sg.Text("", key="-TARGETPRICE-")],
            [sg.Text("Risk ($)", size=(18,1)), sg.Text("", key="-RISKDOLLAR-")],
            [sg.Text("Reward ($)", size=(18,1)), sg.Text("", key="-REWARD-")],
            [sg.Text("Share Size", size=(18,1)), sg.Text("", key="-SHARES-")],
            [sg.Text("Risk/Reward", size=(18,1)), sg.Text("", key="-RR-")],
        ])]
    ]
    chart_col = [[sg.Canvas(key="-CANVAS-")]]
    layout = [
        [sg.Column(input_col, element_justification='left'), sg.VSeparator(), sg.Column(chart_col)]
    ]
    return sg.Window("Risk Calculator", layout, finalize=True, size=(800,600))


def main():
    window = create_window()
    fig, ax = plt.subplots(figsize=(4,4))
    canvas_elem = window["-CANVAS-"]
    fig_agg = FigureCanvasTkAgg(fig, canvas_elem.TKCanvas)
    fig_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    while True:
        event, values = window.read(timeout=100)
        if event == sg.WIN_CLOSED:
            break
        metrics = compute_trade_metrics(values.get("-PRICE-"), values.get("-CAPITAL-"),
                                        float(values.get("-STOP-",1)), float(values.get("-RISK-",1)),
                                        float(values.get("-RATIO-",2)))
        if metrics:
            window["-STOPPRICE-"].update(f"{metrics['stop_price']:.2f}")
            window["-TARGETPRICE-"].update(f"{metrics['target_price']:.2f}")
            window["-RISKDOLLAR-"].update(f"{metrics['risk_per_trade']:.2f}")
            window["-REWARD-"].update(f"{metrics['reward_per_trade']:.2f}")
            window["-SHARES-"].update(f"{metrics['shares']}")
            window["-RR-"].update(f"{metrics['rr_ratio']:.2f}")
            draw_chart(canvas_elem, fig_agg, ax, float(values.get("-PRICE-",0)),
                       metrics['stop_price'], metrics['target_price'])
    window.close()


if __name__ == "__main__":
    main()
