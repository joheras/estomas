import h5py
import os



class HDF5DatasetWriter:

    def __init__(self,dimsI,dimsL,outputPath,dataKey="images",bufSize=1000):
        # check to see if the output path exists, and if so, raise
        # an exception
        if os.path.exists(outputPath):
            raise ValueError("The supplied ‘outputPath‘ already "
                "exists and cannot be overwritten. Manually delete "
                "the file before continuing.", outputPath)

        # open the HDF5 database for writing and create two datasets:
        # one to store the images and another to store the labels
        self.db = h5py.File(outputPath, "w")
        self.data = self.db.create_dataset(dataKey, dimsI,dtype="float")
        self.labels = self.db.create_dataset("labels", dimsL, dtype="float")

        # store the buffer size, then initialize the buffer itself
        # along with the index into the datasets
        self.bufSize = bufSize
        self.buffer = {"data": [], "labels": []}
        self.idx = 0

