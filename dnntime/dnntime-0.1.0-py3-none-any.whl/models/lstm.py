import time
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
# helper functions
from ..utils import print_dynamic_rmse, print_mae, print_mape


def build_lstm_model(X_train, y_train, X_test, y_test, n_input, n_output=1,
                     n_features=1, n_units=64, d_rate=0.15, n_epoch=10, n_batch=1, verbose=0):

    lstm_model = StackedLSTM(n_input, n_output, n_units, n_features, d_rate)
    lstm_model.compile(optimizer="adam", loss="mse")
    start_time = time.time()
    lstm_model.fit(X_train, y_train, epochs=n_epoch, batch_size=n_batch)
    end_time = time.time()

    lstm_pred = lstm_model.predict(X_test)

    rmse, norm_rmse = print_dynamic_rmse(y_test, lstm_pred, y_train)
    mae = print_mae(y_test, lstm_pred)
    mape = print_mape(y_test, lstm_pred)
    run_time = end_time - start_time
    print("-----------------------------------------------------------------")
    print("LSTM SUMMARY:")
    print("-----------------------------------------------------------------")
    print(f"MAE Score: {round(mae, 4)}")
    print(f"MAPE Score: {round(mape, 4)}")
    print(f"RMSE Score: {round(rmse, 4)}")
    print(f"Normalized RMSE Score: {round(norm_rmse, 4)*100}%")
    print(f"Total Training Time: {round(run_time/60, 2)} min")

    return lstm_model, lstm_pred, rmse, norm_rmse


def VanillaLSTM(n_input, n_output, n_units, n_features):
    model = Sequential()
    model.add(LSTM(n_units, activation="tanh", return_sequences=False,
                   input_shape=(n_input, n_features)))
    model.add(Dense(n_output))
    print("Vanilla LSTM model summary:")
    model.summary()
    return model


def StackedLSTM(n_input, n_output, n_units, n_features, d_rate=0.5):
    model = Sequential()
    model.add(LSTM(n_units, activation="tanh", return_sequences=True,
                   input_shape=(n_input, n_features)))
    model.add(Dropout(d_rate))
    model.add(LSTM(n_units, activation="tanh", return_sequences=True))
    model.add(Dropout(d_rate))
    model.add(LSTM(n_units, activation="tanh", return_sequences=False))
    model.add(Dropout(d_rate))
    model.add(Dense(n_output))
    print("Stacked LSTM model summary:")
    model.summary()
    return model


def CustomRNN(n_input, n_output, n_units, n_features):
    pass
