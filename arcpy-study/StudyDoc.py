import arcpy

"""
图表             arcpy.charts
数据访问模块       arcpy.da
地理编码          arcpy.geocoding
影像分析          arcpy.ia
映射             arcpy.mp
元数据           arcpy.metadata
制图模块         arcpy-study.mapping
空间分析模块      arcpy.sa
网络分析模块      arcpy-study.na
工作流管理器      arcpy.wmx
网络分析         arcpy.nax 和 arcpy.na
共享            arcpy.sharing
"""

# 基本使用
"""
# 导入模块
import arcpy

# 设置环境（非必要） 如果在arcgis中运行可使用"CURRENT"
arcpy.env.workspace = "xxx\\xxx.gdb"
"""

# 常用工具箱 arcpy.工具名称_工具箱别名
"""
裁剪工具：arcpy.analysis(被裁剪要素,裁剪要素,结果)
筛选工具：Select_analysis(源数据,结果数据,筛选条件)
相交工具：Intersect_analysis([数据1,数据2],相交结果)
交集取反工具：SymDiff_analysis(对比数据1,对比数据2,结果)
创建文件地理数据库：CreateFileGDB_management(dir,gdbName)
分割工具：Split_analysis(分割图层,用来分割的要素类,分割字段,存储gdbPath)
"""

####################### 示例代码#################################
"""
gdbPath = r"E:\dev-data\gdb\530902临翔区.gdb"
arcpy.env.workspace = gdbPath
# 实现提取
def selectDltb():
    # 定义查询语句
    whereSlq = '"DLBM" = \'011\''
    # 查询数据
    arcpy.Select_analysis("DLTB（2009年二调数据）20180928", "水田2019", whereSlq)
    print("提取二调水田成功")
    # 查询数据
    whereSlq = '"DLBM" = \'0101\''
    arcpy.Select_analysis("DLTB（2021年变更）", "水田2021", whereSlq)
    print("提取三调水田成功")

# 实现获取交集
def intersect():
    arcpy.Intersect_analysis(["水田2019","水田2021"],"相交数据")
    # 提取增加部分
    arcpy.SymDiff_analysis("相交数据","水田2021","增加的水田")
    arcpy.SymDiff_analysis("相交数据","水田2019","减少的水田")

# 创建新的数据并且使用村级行政区分割
def split():
    # 创建数据库
    arcpy.CreateFileGDB_management(r"E:\dev-data\gdb","outList")
    # 进行分割
    arcpy.Split_analysis("减少的水田","XJXZQ","XZQMC",r"E:\dev-data\gdb\outList.gdb")

# 实现提取
selectDltb()
# 获取相交数据
intersect()
# 分割数据
split()
"""
####################### 示例代码#################################

# 空间数据处理
"""
arcpy.Exists(要素类) 要素类是否存在，返回布尔
arcpy.Describe(要素类) 查询要素类的数据,{name,featureType,shapeType}
arcpy.ListDatasets([feature_type='Raster'],[wild_card='A*']) 返回文件夹中的数据列表
arcpy.ListFeatureClasses([wild_card='DLTB*'],[feature_type],[feature_dataset]) 
arcpy.ListFileIds(要素类,[wild_card='xzqmc*'],[field_type])
arcpy.ListFiles(文件夹) 文件列表
arcpy.ListIndexes()
arcpy.ListRasters()
arcpy.ListTables()
arcpy.ListVersions()
arcpy.ListWorkspace()
"""

# 游标
"""
arcpy.da.SearchCursor(要素类,[使用的字段],where_clause 查询sql,spatial_reference 空间参考,explode_to_points 多点多行)  只读访问游标
    fields = ["objectid","SHAPE@AREA"]
arcpy.da.InsertCursor(要素类,[插入字段A,插入字段B])  插入游标
    cursor.insertRow((a,a))
arcpy.da.UpdateCursor(要素类[字段1,字段2])
        cursor.deleteRow(); 删除行
"""
import arcpy

arcpy.env.workspace = r"E:\dev-data\gdb\530902临翔区.gdb"
# 查询数据
cursor = arcpy.SearchCursor("减少的水田", ["YSDM", "TBBH"])
for row in cursor:
    pass

# 使用自定义的工具
"""
arcpy.ImportToolbox("xxx\\xxx.tbx","name")
"""
