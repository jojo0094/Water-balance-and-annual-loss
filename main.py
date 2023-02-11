from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP

from src.components.layout import create_layout
from src.data.loader import load_transaction_data, load_data_dict

DATA_PATH = "./data/transactions.csv"


def main() -> None:

    # load the data and create the data manager
    data = load_transaction_data(DATA_PATH)
    print(data.columns)
    data_dict = load_data_dict(['Waipukurau','Waipawa-Otane','Waipawa-Otance','Takapua','Porangahau-Te Paerahi','Kiarakau'])
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Water Loss and Annnual Balance Dashboard"
    app.layout = create_layout(app, data, data_dict)
    app.run()


if __name__ == "__main__":
    main()
