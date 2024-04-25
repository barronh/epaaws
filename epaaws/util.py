__all__ = ['open_date']


def open_date(
    date, tmpl, bucket, cache=True
):
    """
    Open all files for specific date

    Arguments
    ---------
    date : str
        Date parsable by pandas.to_datetime
    tmpl : str
        strftime template for date file (e.g., MCIP/GRIDCRO2D.12US1.35L.%y%m%d)
    bucket : str
        Bucket to pull from (e.g., )
    cache : bool
        Store file to prevent re-downloading.

    Returns
    -------
    ds : xarray.Dataset
        File opened (either in memory or from disk)
    """
    import boto3
    import pandas as pd
    from botocore import UNSIGNED
    from botocore.client import Config
    import io
    import os
    import cmaqsatproc as csp

    client = boto3.client('s3', config=Config(signature_version=UNSIGNED))
    date = pd.to_datetime(date)
    path = date.strftime(tmpl)
    if cache:
        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path), exist_ok=True)
            client.download_file(bucket, path, path)
        f = csp.open_ioapi(path)
    else:
        obj = client.get_object(Bucket=bucket, Key=path)
        bdy = io.BytesIO(obj['Body'].read())
        f = csp.open_ioapi(bdy, engine='scipy')
    return f
