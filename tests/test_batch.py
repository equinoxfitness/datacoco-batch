import unittest
from datacoco_batch.batch import Batch


class TestBatch(unittest.TestCase):

    test_wf = "cc3_test_wf"

    @classmethod
    def setUpClass(cls):
        cls.batchy = Batch(
            wf=cls.test_wf,
            server="hypergate-services.equinoxfitness.com",
            port="80",
        )

    def test_open_batch(self):  # "status": "open"
        resp = self.batchy.open()
        status = resp["global"]["status"]
        self.assertEqual(status, "open")

    def test_get_status(self):
        expected_keys = ["global"]
        resp = self.batchy.get_status()
        self.assertEqual(list(resp.keys()), expected_keys)

    def test_close_batch(self):  # "status": "success"
        resp = self.batchy.close()
        status = resp["global"]["status"]

        self.assertEqual(status, "success")

    def test_fail_batch(self):  # "status": "failure"
        resp = self.batchy.fail()
        status = resp["global"]["status"]

        self.assertEqual(status, "failure")

    def test_get_status_summary(self):
        expected_keys = [
            "batch_id",
            "status",
            "failure_cnt",
            "open_cnt",
            "batch_start",
            "batch_end",
        ]
        resp = self.batchy.get_status_summary()
        self.assertEqual(list(resp.keys()), expected_keys)
