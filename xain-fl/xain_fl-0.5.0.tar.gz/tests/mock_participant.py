import argparse

from xain_sdk.participant_state_machine import start_participant


class MockLocalParticipant:
    def __init__(self, offset=1):
        self.offset = offset

    def train_round(self, weights, epochs, epoch_base):
        print(f"received: {weights}")
        # theta_next = [nda + self.offset for nda in weights]
        theta_next = weights
        num_samples = 1
        mets = {}
        print(f"trained: {theta_next}")
        return theta_next, num_samples, mets

    def metrics(self):
        cid = 0
        vbc = []
        return cid, vbc


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mock Participant CLI")
    parser.add_argument("-o", dest="offset", default=1, type=int, help="offset to apply to model")
    params = parser.parse_args()
    part = MockLocalParticipant(offset=params.offset)
    start_participant(part, "localhost:50051")
