from sklearn.ensemble import IsolationForest
import numpy as np

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1)
        self.is_trained = False

    def train(self, historical_data):
        try:
            X = np.array([
                [item['cpu'], item['memory'], item['network']['connections']]
                for item in historical_data
                if 'cpu' in item and 'memory' in item and 'network' in item and 'connections' in item['network']
            ])
            self.model.fit(X)
            self.is_trained = True
        except KeyError as e:
            print(f"⚠️ Missing data key: {e}")
        except Exception as e:
            print(f"⚠️ Error during training: {e}")

    def detect_anomaly(self, current_stats):
        if not self.is_trained:
            print("⚠️ Model is not trained.")
            return False

        try:
            X = np.array([[
                current_stats['cpu'],
                current_stats['memory'],
                current_stats['network']['connections']
            ]])
            return self.model.predict(X)[0] == -1
        except KeyError as e:
            print(f"⚠️ Missing data key: {e}")
            return False
        except Exception as e:
            print(f"⚠️ Error while detecting anomaly: {e}")
            return False