from sqlalchemy import create_engine, text

engine = create_engine(
    "mysql+pymysql://admin:1234admin@database-3.cnmq0wo4g64z.eu-north-1.rds.amazonaws.com/bmembers?charset=utf8mb4"
)
with engine.connect() as conn:
  result = conn.execute(text("select * from trial"))
  print(result.all())
#interaction between mysql and python