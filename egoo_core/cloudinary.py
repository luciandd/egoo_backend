import cloudinary
import cloudinary.uploader

class CloudinaryUploader():
  def __init__(self, file, folder, public_id, resource_type="image"):
    self.file = file
    self.folder = folder
    self.public_id = public_id
    self.resource_type = resource_type

  def upload(self):
    return cloudinary.uploader.upload(
      self.file,
      folder=self.folder,
      public_id=self.public_id,
      resource_type=self.resource_type, 
      overwrite=True,
    )

class Test():
  def __init__(self):
    pass
  def test(self):
    pass

  def test2(self):
    pass
  def test3(self):
    pass