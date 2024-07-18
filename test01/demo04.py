# -*- coding: utf-8 -*-
import os
import numpy
from osgeo import gdal

class GRID:
    #读图像文件
    def read_img(self,filename):
        dataset=gdal.Open(filename)       #打开文件

        im_width = dataset.RasterXSize    #栅格矩阵的列数
        im_height = dataset.RasterYSize   #栅格矩阵的行数

        im_geotrans = dataset.GetGeoTransform()  #仿射矩阵
        im_proj = dataset.GetProjection() #地图投影信息
        im_data = dataset.ReadAsArray(0,0,im_width,im_height) #将数据写成数组，对应栅格矩阵

        del dataset
        return im_proj,im_geotrans,im_data

    #写文件，以写成tif为例
    def write_img(self,filename,im_proj,im_geotrans,im_data):
        #gdal数据类型包括
        #gdal.GDT_Byte,
        #gdal .GDT_UInt16, gdal.GDT_Int16, gdal.GDT_UInt32, gdal.GDT_Int32,
        #gdal.GDT_Float32, gdal.GDT_Float64

        #判断栅格数据的数据类型
        if 'int8' in im_data.dtype.name:
            datatype = gdal.GDT_Byte
        elif 'int16' in im_data.dtype.name:
            datatype = gdal.GDT_UInt16
        else:
            datatype = gdal.GDT_Float32

        #判读数组维数
        if len(im_data.shape) == 3:
            im_bands, im_height, im_width = im_data.shape
        else:
            im_bands, (im_height, im_width) = 1,im_data.shape

            #创建文件
        driver = gdal.GetDriverByName("GTiff")            #数据类型必须有，因为要计算需要多大内存空间
        dataset = driver.Create(filename, im_width, im_height, im_bands, datatype)

        dataset.SetGeoTransform(im_geotrans)              #写入仿射变换参数
        dataset.SetProjection(im_proj)                    #写入投影

        if im_bands == 1:
            dataset.GetRasterBand(1).WriteArray(im_data)  #写入数组数据
        else:
            for i in range(im_bands):
                dataset.GetRasterBand(i+1).WriteArray(im_data[i])

        del dataset

# 定义影像文件路径
image_path = r'E:\gis-data\服务器拷贝\E实景三维\E1收集原始数据\A1普洱市\影像\思茅区城区高清谷歌影像\思茅区城区高清谷歌影像.tif'

if __name__ == "__main__":
    os.chdir(r'E:/data')                        #切换路径到待处理图像所在文件夹
    proj,geotrans,data = GRID().read_img(image_path)        #读数据
    print(proj)
    print(geotrans)
    #print(data)
    print(data.shape)
    channel,width,height = data.shape
    for i in range(width//256):#切割成256*256小图
        for j in range(height//256):
            cur_image = data[:,i*256:(i+1)*256,j*256:(j+1)*256]
            GRID().write_img(r'E:\gis-data\服务器拷贝\E实景三维\E1收集原始数据\A1普洱市\影像\思茅区城区高清谷歌影像\raw1\{}_{}.tif'.format(i,j),proj,geotrans,cur_image) ##写数据
