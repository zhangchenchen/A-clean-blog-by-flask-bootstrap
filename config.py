#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__)) 

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'meiyoushezhimima'
    SQLALCHEMY_COMMIT_ON_REARDOWN = True


    @staticmethod
    def init_app(app):
        pass

class ProductionConfig(Config):
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    dbhost = 'pekingzccdb.cjiwhis5e4uf.us-west-2.rds.amazonaws.com'  
    dbuser = 'pekingzcc' ### 
    dbpass = 'zhangchen130826'  
    dbname = 'pekingzcc'   
    SQLALCHEMY_DATABASE_URI = 'mysql://' + dbuser  + ':' + dbpass + '@' + dbhost + '/' + dbname  

config = {
    'production':ProductionConfig,
    'default':ProductionConfig
}