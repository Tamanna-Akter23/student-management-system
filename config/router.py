class DatabaseRouter:
    route_app_labels={'courses'}
    def db_for_read(self,model,**hints): return 'postgres' if model._meta.app_label in self.route_app_labels else 'default'
    def db_for_write(self,model,**hints): return 'postgres' if model._meta.app_label in self.route_app_labels else 'default'
    def allow_relation(self,obj1,obj2,**hints): return True
    def allow_migrate(self,db,app_label,model_name=None,**hints):
        if app_label in self.route_app_labels: return db=='postgres'
        return db=='default'
