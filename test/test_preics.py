import logging

def test_job_executor(caplog):
    caplog.set_level(logging.INFO)
    logging.info("Started")
