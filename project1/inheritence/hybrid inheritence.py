class company:
    def __init__(self,req):
        self.req=req
class development(company):
    def __init__(self,dev_id,test_id,req):
        self.dev_id=dev_id
        super().__init__(test_id,req)
class testing(company):
    def __init__(self,test_id,req):
        self.test_id=test_id
        super().__init__(req)
class project(development,testing):
    def __init__(self,project_name,project_id,dev_id,test_id,req):
        self.project_name=project_name
        self.project_id=project_id
        super().__init__(dev_id,test_id,req)
#calling block
p1=project("prasad",'11122','344','666','222')
p2=project("naidu",'112332','444','44444','34434')
print(p1)
print(p1.project_name,p1.project_id,p1.dev_id,p1.test_id,p1.req)
print("-----------------------------------------")
print(p2.project_name,p2.project_id,p2.dev_id,p2.test_id,p2.req)
