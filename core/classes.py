# coding: utf-8


class CoreRouter(object):
    """
       A router to control all database operations on models in the
       auth application.
       """

    def db_for_read(self, model, **hints):
        """
        Указываем из какой базы читаем кладр
        """
        if model._meta.app_label == 'core':
            return 'conf'
        return None

    def db_for_write(self, model, **hints):
        """
        Указываем в какую базу пишем кладр
        """
        if model._meta.app_label == 'core':
            return 'conf'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Подтверждаем связи в нутри приложения кладр
        """
        if obj1._meta.app_label == 'core' or obj2._meta.app_label == 'core':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'auth_db'
        database.
        """
        if app_label == 'core':
            return db == 'conf'
        return None

    def allow_syncdb(self, db, model):
        return True