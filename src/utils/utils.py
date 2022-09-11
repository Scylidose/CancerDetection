from tciaclient.core import TCIAClient


def download_datasets():
    download_tcia_dataset("RIDER Breast MRI", "MR")
    
    
def download_tcia_dataset(collection_name, modality):
    tc = TCIAClient()

    series = tc.get_series(collection=collection_name, modality=modality)

    download_path = "./data/mri/tcia-downloads"
    for i, s in enumerate(series):
        print(str(i).zfill(3)+"-"+collection_name + " DOWNLOADED")
        tc.get_image(seriesInstanceUid = s["SeriesInstanceUID"],
            downloadPath = download_path, zipFileName = str(i).zfill(3)+"-"+collection_name+".zip")