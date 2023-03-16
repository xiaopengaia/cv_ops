import torch

def upsample_bilinear(src_data, shape, align_corners):
  
  batch, channel, src_height, src_width = src_data.shape
  dst_height, dst_width = shape
  
  dst_data = torch.zeros((batch, channel, dst_height, dst_width))
  
  
  
  
