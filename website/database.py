from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# Tạo một đối tượng engine để kết nối đến cơ sở dữ liệu MySQL
engine = create_engine('mysql+pymysql://username:password@localhost/databasename')

# Tạo một đối tượng metadata để đại diện cho các bảng trong cơ sở dữ liệu
metadata = MetaData()

# Tạo một bảng mới
new_table = Table(
    'new_table',  # Tên của bảng
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('age', Integer)
)

# Tạo bảng trong cơ sở dữ liệu
metadata.create_all(engine)

# Đóng kết nối
engine.dispose()
