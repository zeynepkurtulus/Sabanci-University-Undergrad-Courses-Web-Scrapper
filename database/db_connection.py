from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import json
import os

cs_file_paths = ["/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Area Courses/BSCS_201801_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Area Courses/BSCS_201802_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Area Courses/BSCS_201901_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Area Courses/BSCS_201902_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Area Courses/BSCS_202001_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Area Courses/BSCS_202002_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Area Courses/BSCS_202101_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Area Courses/BSCS_202102_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Area Courses/BSCS_202201_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Area Courses/BSCS_202202_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Area Courses/BSCS_202301_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Area Courses/BSCS_202302_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Core Courses/BSCS_201801_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Core Courses/BSCS_201802_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Core Courses/BSCS_201901_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Core Courses/BSCS_201902_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Core Courses/BSCS_202001_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Core Courses/BSCS_202002_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Core Courses/BSCS_202101_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Core Courses/BSCS_202102_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Core Courses/BSCS_202201_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Core Courses/BSCS_202202_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Core Courses/BSCS_202301_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Core Courses/BSCS_202302_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Free Courses/BSCS_201801_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Free Courses/BSCS_201802_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Free Courses/BSCS_201901_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Free Courses/BSCS_201902_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Free Courses/BSCS_202001_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Free Courses/BSCS_202002_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Free Courses/BSCS_202101_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Free Courses/BSCS_202102_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Free Courses/BSCS_202201_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Free Courses/BSCS_202202_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Free Courses/BSCS_202301_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Free Courses/BSCS_202302_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Required Courses/BSCS_201801_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Required Courses/BSCS_201802_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Required Courses/BSCS_201901_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Required Courses/BSCS_201902_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Required Courses/BSCS_202001_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Required Courses/BSCS_202002_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Required Courses/BSCS_202101_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Required Courses/BSCS_202102_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Required Courses/BSCS_202201_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Required Courses/BSCS_202202_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Required Courses/BSCS_202301_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Required Courses/BSCS_202302_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Basic Science and Engineering Courses/BSCS_201801_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Basic Science and Engineering Courses/BSCS_201802_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Basic Science and Engineering Courses/BSCS_201901_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Basic Science and Engineering Courses/BSCS_201902_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Basic Science and Engineering Courses/BSCS_202001_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Basic Science and Engineering Courses/BSCS_202002_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Basic Science and Engineering Courses/BSCS_202101_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Basic Science and Engineering Courses/BSCS_202102_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Basic Science and Engineering Courses/BSCS_202201_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Basic Science and Engineering Courses/BSCS_202202_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Basic Science and Engineering Courses/BSCS_202301_CatReq.json",
              "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSCS/Basic Science and Engineering Courses/BSCS_202302_CatReq.json"] 
ie_file_paths = ["/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Area Courses/BSMS_201801_CatReq.json",
                 "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Area Courses/BSMS_201802_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Area Courses/BSMS_201901_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Area Courses/BSMS_201902_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Area Courses/BSMS_202001_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Area Courses/BSMS_202002_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Area Courses/BSMS_202101_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Area Courses/BSMS_202102_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Area Courses/BSMS_202201_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Area Courses/BSMS_202202_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Area Courses/BSMS_202301_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Area Courses/BSMS_202302_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Core Courses/BSMS_201801_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Core Courses/BSMS_201802_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Core Courses/BSMS_201901_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Core Courses/BSMS_201902_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Core Courses/BSMS_202001_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Core Courses/BSMS_202002_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Core Courses/BSMS_202101_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Core Courses/BSMS_202102_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Core Courses/BSMS_202201_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Core Courses/BSMS_202202_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Core Courses/BSMS_202301_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Core Courses/BSMS_202302_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Free Courses/BSMS_201801_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Free Courses/BSMS_201802_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Free Courses/BSMS_201901_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Free Courses/BSMS_201902_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Free Courses/BSMS_202001_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Free Courses/BSMS_202002_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Free Courses/BSMS_202101_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Free Courses/BSMS_202102_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Free Courses/BSMS_202201_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Free Courses/BSMS_202202_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Free Courses/BSMS_202301_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Free Courses/BSMS_202302_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Required Courses/BSMS_201801_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Required Courses/BSMS_201802_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Required Courses/BSMS_201901_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Required Courses/BSMS_201902_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Required Courses/BSMS_202001_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Required Courses/BSMS_202002_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Required Courses/BSMS_202101_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Required Courses/BSMS_202102_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Required Courses/BSMS_202201_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Required Courses/BSMS_202202_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Required Courses/BSMS_202301_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Required Courses/BSMS_202302_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Basic Science and Engineering Courses/BSMS_201801_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Basic Science and Engineering Courses/BSMS_201802_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Basic Science and Engineering Courses/BSMS_201901_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Basic Science and Engineering Courses/BSMS_201902_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Basic Science and Engineering Courses/BSMS_202001_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Basic Science and Engineering Courses/BSMS_202002_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Basic Science and Engineering Courses/BSMS_202101_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Basic Science and Engineering Courses/BSMS_202102_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Basic Science and Engineering Courses/BSMS_202201_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Basic Science and Engineering Courses/BSMS_202202_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Basic Science and Engineering Courses/BSMS_202301_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMS/Basic Science and Engineering Courses/BSMS_202302_CatReq.json"]
me_file_paths = ["/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Area Courses/BSME_201801_CatReq.json",
                 "Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Area Courses/BSME_201802_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Area Courses/BSME_201901_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Area Courses/BSME_201902_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Area Courses/BSME_202001_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Area Courses/BSME_202002_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Area Courses/BSME_202101_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Area Courses/BSME_202102_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Area Courses/BSME_202201_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Area Courses/BSME_202202_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Area Courses/BSME_202301_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Area Courses/BSME_202302_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Core Courses/BSME_201801_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Core Courses/BSME_201802_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Core Courses/BSME_201901_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Core Courses/BSME_201902_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Core Courses/BSME_202001_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Core Courses/BSME_202002_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Core Courses/BSME_202101_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Core Courses/BSME_202102_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Core Courses/BSME_202201_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Core Courses/BSME_202202_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Core Courses/BSME_202301_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Core Courses/BSME_202302_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Free Courses/BSME_201801_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Free Courses/BSME_201802_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Free Courses/BSME_201901_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Free Courses/BSME_201902_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Free Courses/BSME_202001_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Free Courses/BSME_202002_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Free Courses/BSME_202101_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Free Courses/BSME_202102_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Free Courses/BSME_202201_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Free Courses/BSME_202202_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Free Courses/BSME_202301_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Free Courses/BSME_202302_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Required Courses/BSME_201801_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Required Courses/BSME_201802_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Required Courses/BSME_201901_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Required Courses/BSME_201902_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Required Courses/BSME_202001_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Required Courses/BSME_202002_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Required Courses/BSME_202101_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Required Courses/BSME_202102_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Required Courses/BSME_202201_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Required Courses/BSME_202202_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Required Courses/BSME_202301_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Required Courses/BSME_202302_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Basic Science and Engineering Courses/BSME_201801_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Basic Science and Engineering Courses/BSME_201802_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Basic Science and Engineering Courses/BSME_201901_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Basic Science and Engineering Courses/BSME_201902_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Basic Science and Engineering Courses/BSME_202001_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Basic Science and Engineering Courses/BSME_202002_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Basic Science and Engineering Courses/BSME_202101_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Basic Science and Engineering Courses/BSME_202102_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Basic Science and Engineering Courses/BSME_202201_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Basic Science and Engineering Courses/BSME_202202_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Basic Science and Engineering Courses/BSME_202301_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSME/Basic Science and Engineering Courses/BSME_202302_CatReq.json"]
ee_file_paths = ["/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Area Courses/BSEE_201801_CatReq.json",
                 "Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Area Courses/BSEE_201802_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Area Courses/BSEE_201901_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Area Courses/BSEE_201902_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Area Courses/BSEE_202001_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Area Courses/BSEE_202002_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Area Courses/BSEE_202101_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Area Courses/BSEE_202102_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Area Courses/BSEE_202201_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Area Courses/BSEE_202202_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Area Courses/BSEE_202301_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Area Courses/BSEE_202302_CatReq.json",   
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Core Courses/BSEE_201801_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Core Courses/BSEE_201802_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Core Courses/BSEE_201901_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Core Courses/BSEE_201902_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Core Courses/BSEE_202001_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Core Courses/BSEE_202002_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Core Courses/BSEE_202101_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Core Courses/BSEE_202102_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Core Courses/BSEE_202201_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Core Courses/BSEE_202202_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Core Courses/BSEE_202301_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Core Courses/BSEE_202302_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Free Courses/BSEE_201801_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Free Courses/BSEE_201802_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Free Courses/BSEE_201901_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Free Courses/BSEE_201902_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Free Courses/BSEE_202001_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Free Courses/BSEE_202002_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Free Courses/BSEE_202101_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Free Courses/BSEE_202102_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Free Courses/BSEE_202201_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Free Courses/BSEE_202202_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Free Courses/BSEE_202301_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Free Courses/BSEE_202302_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Required Courses/BSEE_201801_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Required Courses/BSEE_201802_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Required Courses/BSEE_201901_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Required Courses/BSEE_201902_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Required Courses/BSEE_202001_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Required Courses/BSEE_202002_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Required Courses/BSEE_202101_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Required Courses/BSEE_202102_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Required Courses/BSEE_202201_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Required Courses/BSEE_202202_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Required Courses/BSEE_202301_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Required Courses/BSEE_202302_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Basic Science and Engineering Courses/BSEE_201801_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Basic Science and Engineering Courses/BSEE_201802_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Basic Science and Engineering Courses/BSEE_201901_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Basic Science and Engineering Courses/BSEE_201902_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Basic Science and Engineering Courses/BSEE_202001_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Basic Science and Engineering Courses/BSEE_202002_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Basic Science and Engineering Courses/BSEE_202101_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Basic Science and Engineering Courses/BSEE_202102_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Basic Science and Engineering Courses/BSEE_202201_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Basic Science and Engineering Courses/BSEE_202202_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Basic Science and Engineering Courses/BSEE_202301_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSEE/Basic Science and Engineering Courses/BSEE_202302_CatReq.json"]
mat_file_paths = ["/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Area Courses/BSMAT_201801_CatReq.json",
                  "Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Area Courses/BSMAT_201802_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Area Courses/BSMAT_201901_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Area Courses/BSMAT_201902_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Area Courses/BSMAT_202001_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Area Courses/BSMAT_202002_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Area Courses/BSMAT_202101_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Area Courses/BSMAT_202102_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Area Courses/BSMAT_202201_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Area Courses/BSMAT_202202_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Area Courses/BSMAT_202301_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Area Courses/BSMAT_202302_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Core Courses/BSMAT_201801_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Core Courses/BSMAT_201802_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Core Courses/BSMAT_201901_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Core Courses/BSMAT_201902_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Core Courses/BSMAT_202001_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Core Courses/BSMAT_202002_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Core Courses/BSMAT_202101_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Core Courses/BSMAT_202102_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Core Courses/BSMAT_202201_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Core Courses/BSMAT_202202_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Core Courses/BSMAT_202301_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Core Courses/BSMAT_202302_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Free Courses/BSMAT_201801_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Free Courses/BSMAT_201802_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Free Courses/BSMAT_201901_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Free Courses/BSMAT_201902_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Free Courses/BSMAT_202001_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Free Courses/BSMAT_202002_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Free Courses/BSMAT_202101_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Free Courses/BSMAT_202102_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Free Courses/BSMAT_202201_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Free Courses/BSMAT_202202_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Free Courses/BSMAT_202301_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Free Courses/BSMAT_202302_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Required Courses/BSMAT_201801_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Required Courses/BSMAT_201802_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Required Courses/BSMAT_201901_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Required Courses/BSMAT_201902_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Required Courses/BSMAT_202001_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Required Courses/BSMAT_202002_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Required Courses/BSMAT_202101_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Required Courses/BSMAT_202102_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Required Courses/BSMAT_202201_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Required Courses/BSMAT_202202_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Required Courses/BSMAT_202301_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Required Courses/BSMAT_202302_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Basic Science and Engineering Courses/BSMAT_201801_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Basic Science and Engineering Courses/BSMAT_201802_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Basic Science and Engineering Courses/BSMAT_201901_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Basic Science and Engineering Courses/BSMAT_201902_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Basic Science and Engineering Courses/BSMAT_202001_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Basic Science and Engineering Courses/BSMAT_202002_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Basic Science and Engineering Courses/BSMAT_202101_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Basic Science and Engineering Courses/BSMAT_202102_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Basic Science and Engineering Courses/BSMAT_202201_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Basic Science and Engineering Courses/BSMAT_202202_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Basic Science and Engineering Courses/BSMAT_202301_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSMAT/Basic Science and Engineering Courses/BSMAT_202302_CatReq.json"]
bio_file_paths = ["/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Area Courses/BSBIO_201801_CatReq.json",
                    "Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Area Courses/BSBIO_201802_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Area Courses/BSBIO_201901_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Area Courses/BSBIO_201902_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Area Courses/BSBIO_202001_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Area Courses/BSBIO_202002_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Area Courses/BSBIO_202101_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Area Courses/BSBIO_202102_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Area Courses/BSBIO_202201_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Area Courses/BSBIO_202202_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Area Courses/BSBIO_202301_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Area Courses/BSBIO_202302_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Core Courses/BSBIO_201801_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Core Courses/BSBIO_201802_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Core Courses/BSBIO_201901_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Core Courses/BSBIO_201902_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Core Courses/BSBIO_202001_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Core Courses/BSBIO_202002_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Core Courses/BSBIO_202101_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Core Courses/BSBIO_202102_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Core Courses/BSBIO_202201_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Core Courses/BSBIO_202202_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Core Courses/BSBIO_202301_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Core Courses/BSBIO_202302_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Free Courses/BSBIO_201801_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Free Courses/BSBIO_201802_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Free Courses/BSBIO_201901_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Free Courses/BSBIO_201902_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Free Courses/BSBIO_202001_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Free Courses/BSBIO_202002_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Free Courses/BSBIO_202101_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Free Courses/BSBIO_202102_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Free Courses/BSBIO_202201_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Free Courses/BSBIO_202202_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Free Courses/BSBIO_202301_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Free Courses/BSBIO_202302_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Required Courses/BSBIO_201801_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Required Courses/BSBIO_201802_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Required Courses/BSBIO_201901_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Required Courses/BSBIO_201902_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Required Courses/BSBIO_202001_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Required Courses/BSBIO_202002_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Required Courses/BSBIO_202101_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Required Courses/BSBIO_202102_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Required Courses/BSBIO_202201_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Required Courses/BSBIO_202202_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Required Courses/BSBIO_202301_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Required Courses/BSBIO_202302_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Basic Science and Engineering Courses/BSBIO_201801_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Basic Science and Engineering Courses/BSBIO_201802_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Basic Science and Engineering Courses/BSBIO_201901_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Basic Science and Engineering Courses/BSBIO_201902_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Basic Science and Engineering Courses/BSBIO_202001_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Basic Science and Engineering Courses/BSBIO_202002_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Basic Science and Engineering Courses/BSBIO_202101_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Basic Science and Engineering Courses/BSBIO_202102_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Basic Science and Engineering Courses/BSBIO_202201_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Basic Science and Engineering Courses/BSBIO_202202_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Basic Science and Engineering Courses/BSBIO_202301_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BSBIO/Basic Science and Engineering Courses/BSBIO_202302_CatReq.json"]
man_file_paths = ["/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Area Courses/BAMAN_201801_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Area Courses/BAMAN_201802_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Area Courses/BAMAN_201901_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Area Courses/BAMAN_201902_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Area Courses/BAMAN_202001_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Area Courses/BAMAN_202002_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Area Courses/BAMAN_202101_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Area Courses/BAMAN_202102_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Area Courses/BAMAN_202201_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Area Courses/BAMAN_202202_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Area Courses/BAMAN_202301_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Area Courses/BAMAN_202302_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Core Courses/BAMAN_201801_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Core Courses/BAMAN_201802_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Core Courses/BAMAN_201901_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Core Courses/BAMAN_201902_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Core Courses/BAMAN_202001_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Core Courses/BAMAN_202002_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Core Courses/BAMAN_202101_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Core Courses/BAMAN_202102_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Core Courses/BAMAN_202201_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Core Courses/BAMAN_202202_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Core Courses/BAMAN_202301_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Core Courses/BAMAN_202302_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Free Courses/BAMAN_201801_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Free Courses/BAMAN_201802_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Free Courses/BAMAN_201901_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Free Courses/BAMAN_201902_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Free Courses/BAMAN_202001_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Free Courses/BAMAN_202002_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Free Courses/BAMAN_202101_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Free Courses/BAMAN_202102_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Free Courses/BAMAN_202201_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Free Courses/BAMAN_202202_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Free Courses/BAMAN_202301_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Free Courses/BAMAN_202302_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Required Courses/BAMAN_201801_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Required Courses/BAMAN_201802_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Required Courses/BAMAN_201901_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Required Courses/BAMAN_201902_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Required Courses/BAMAN_202001_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Required Courses/BAMAN_202002_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Required Courses/BAMAN_202101_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Required Courses/BAMAN_202102_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Required Courses/BAMAN_202201_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Required Courses/BAMAN_202202_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Required Courses/BAMAN_202301_CatReq.json",
                "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAMAN/Required Courses/BAMAN_202302_CatReq.json"]
psy_file_paths = ["/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Area Courses/BAPSY_201801_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Area Courses/BAPSY_201802_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Area Courses/BAPSY_201901_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Area Courses/BAPSY_201902_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Area Courses/BAPSY_202001_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Area Courses/BAPSY_202002_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Area Courses/BAPSY_202101_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Area Courses/BAPSY_202102_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Area Courses/BAPSY_202201_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Area Courses/BAPSY_202202_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Area Courses/BAPSY_202301_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Area Courses/BAPSY_202302_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Core Courses/BAPSY_201801_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Core Courses/BAPSY_201802_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Core Courses/BAPSY_201901_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Core Courses/BAPSY_201902_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Core Courses/BAPSY_202001_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Core Courses/BAPSY_202002_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Core Courses/BAPSY_202101_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Core Courses/BAPSY_202102_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Core Courses/BAPSY_202201_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Core Courses/BAPSY_202202_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Core Courses/BAPSY_202301_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Core Courses/BAPSY_202302_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Free Courses/BAPSY_201801_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Free Courses/BAPSY_201802_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Free Courses/BAPSY_201901_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Free Courses/BAPSY_201902_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Free Courses/BAPSY_202001_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Free Courses/BAPSY_202002_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Free Courses/BAPSY_202101_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Free Courses/BAPSY_202102_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Free Courses/BAPSY_202201_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Free Courses/BAPSY_202202_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Free Courses/BAPSY_202301_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Free Courses/BAPSY_202302_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Required Courses/BAPSY_201801_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Required Courses/BAPSY_201802_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Required Courses/BAPSY_201901_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Required Courses/BAPSY_201902_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Required Courses/BAPSY_202001_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Required Courses/BAPSY_202002_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Required Courses/BAPSY_202101_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Required Courses/BAPSY_202102_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Required Courses/BAPSY_202201_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Required Courses/BAPSY_202202_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Required Courses/BAPSY_202301_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Required Courses/BAPSY_202302_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492/ web scrapping major req/BAPSY/Philosophy Requirement Courses/BAPSY_201801_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Philosophy Requirement Courses/BAPSY_201802_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Philosophy Requirement Courses/BAPSY_201901_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Philosophy Requirement Courses/BAPSY_201902_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Philosophy Requirement Courses/BAPSY_202001_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Philosophy Requirement Courses/BAPSY_202002_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Philosophy Requirement Courses/BAPSY_202101_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Philosophy Requirement Courses/BAPSY_202102_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Philosophy Requirement Courses/BAPSY_202201_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Philosophy Requirement Courses/BAPSY_202202_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Philosophy Requirement Courses/BAPSY_202301_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAPSY/Philosophy Requirement Courses/BAPSY_202302_CatReq.json"]
econ_file_paths = ["/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Area Courses/BAECON_201801_CatReq.json",
                     "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Area Courses/BAECON_201802_CatReq.json",
                      "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Area Courses/BAECON_201901_CatReq.json",
                      "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Area Courses/BAECON_201902_CatReq.json",
                      "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Area Courses/BAECON_202001_CatReq.json",
                      "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Area Courses/BAECON_202002_CatReq.json",
                      "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Area Courses/BAECON_202101_CatReq.json",
                      "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Area Courses/BAECON_202102_CatReq.json",
                      "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Area Courses/BAECON_202201_CatReq.json",
                      "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Area Courses/BAECON_202202_CatReq.json",
                      "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Area Courses/BAECON_202301_CatReq.json",
                      "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Area Courses/BAECON_202302_CatReq.json",
                      "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Core Courses/BAECON_201801_CatReq.json",
                      "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Core Courses/BAECON_201802_CatReq.json",
                      "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Core Courses/BAECON_201901_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Core Courses/BAECON_201902_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Core Courses/BAECON_202001_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Core Courses/BAECON_202002_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Core Courses/BAECON_202101_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Core Courses/BAECON_202102_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Core Courses/BAECON_202201_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Core Courses/BAECON_202202_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Core Courses/BAECON_202301_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Core Courses/BAECON_202302_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Free Courses/BAECON_201801_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Free Courses/BAECON_201802_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Free Courses/BAECON_201901_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Free Courses/BAECON_201902_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Free Courses/BAECON_202001_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Free Courses/BAECON_202002_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Free Courses/BAECON_202101_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Free Courses/BAECON_202102_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Free Courses/BAECON_202201_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Free Courses/BAECON_202202_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Free Courses/BAECON_202301_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Free Courses/BAECON_202302_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Required Courses/BAECON_201801_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Required Courses/BAECON_201802_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Required Courses/BAECON_201901_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Required Courses/BAECON_201902_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Required Courses/BAECON_202001_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Required Courses/BAECON_202002_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Required Courses/BAECON_202101_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Required Courses/BAECON_202102_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Required Courses/BAECON_202201_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Required Courses/BAECON_202202_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Required Courses/BAECON_202301_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAECON/Required Courses/BAECON_202302_CatReq.json"]
vacd_file_paths = ["/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Area Courses/BAVACD_201801_CatReq.json",
                    "Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Area Courses/BAVACD_201802_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Area Courses/BAVACD_201901_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Area Courses/BAVACD_201902_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Area Courses/BAVACD_202001_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Area Courses/BAVACD_202002_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Area Courses/BAVACD_202101_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Area Courses/BAVACD_202102_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Area Courses/BAVACD_202201_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Area Courses/BAVACD_202202_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Area Courses/BAVACD_202301_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Area Courses/BAVACD_202302_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Core Courses/BAVACD_201801_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Core Courses/BAVACD_201802_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Core Courses/BAVACD_201901_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Core Courses/BAVACD_201902_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Core Courses/BAVACD_202001_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Core Courses/BAVACD_202002_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Core Courses/BAVACD_202101_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Core Courses/BAVACD_202102_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Core Courses/BAVACD_202201_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Core Courses/BAVACD_202202_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Core Courses/BAVACD_202301_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Core Courses/BAVACD_202302_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Free Courses/BAVACD_201801_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Free Courses/BAVACD_201802_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Free Courses/BAVACD_201901_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Free Courses/BAVACD_201902_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Free Courses/BAVACD_202001_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Free Courses/BAVACD_202002_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Free Courses/BAVACD_202101_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Free Courses/BAVACD_202102_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Free Courses/BAVACD_202201_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Free Courses/BAVACD_202202_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Free Courses/BAVACD_202301_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Free Courses/BAVACD_202302_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Required Courses/BAVACD_201801_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Required Courses/BAVACD_201802_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Required Courses/BAVACD_201901_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Required Courses/BAVACD_201902_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Required Courses/BAVACD_202001_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Required Courses/BAVACD_202002_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Required Courses/BAVACD_202101_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Required Courses/BAVACD_202102_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Required Courses/BAVACD_202201_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Required Courses/BAVACD_202202_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Required Courses/BAVACD_202301_CatReq.json",
                    "/Users/zeynepkurtulus/Desktop/ens492 web scrapping major req/BAVACD/Required Courses/BAVACD_202302_CatReq.json"]



                 

def connect_to_mongodb(uri):
    try:
        client = MongoClient(uri)
        print("Connected to MongoDB Atlas successfully!")
        return client
    except ConnectionFailure:
        print("Failed to connect to MongoDB Atlas.")
        return None
    


def read_json_file(file_path):
    try:
        with open(file_path, "r", encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None
    

def insert_data_to_collection(client, database_name, collection_name, data):
    db = client[database_name]  # Access the database
    collection = db[collection_name]  # Access the collection

    # Insert the data into the collection
    result = collection.insert_many(data)
    print(f"{len(result.inserted_ids)} documents inserted successfully.")


def create_collection(client, database_name, collection_name):
    if client:
        try:
            db = client.get_database(database_name)
            if collection_name not in db.list_collection_names():
                db.create_collection(collection_name)
                print(f"Collection '{collection_name}' created in database '{database_name}'")
            else:
                print(f"Collection '{collection_name}' already exists in database '{database_name}'")
            return db.get_collection(collection_name)
        except Exception as e:
            print(f"Failed to create or access collection: {e}")
            return None
    else:
        print("MongoDB client is not connected.")
        return None


# INSERT CS COURSES FUNCTION 
def insert_courses(json_data, client, database, collection_name):
    data = read_json_file(json_data)
    if data:
        insert_data_to_collection(client, database, collection_name, data)
    else:
        print(f"No data to insert for {collection_name}")



# Example usage
uri = "mongodb+srv://zeynepkrtls01:ZRAZ2x5rw9AXMllc@sugradcluster.aro7tnh.mongodb.net/"
client = connect_to_mongodb(uri)
collection_names = ["CS-201801", "CS-201802", "CS-201901", "CS-201902", "CS-202001", "CS-202002", "CS-202101", "CS-202102", "CS-202201", "CS-202202", "CS-202301", "CS-202302",
                    "CS-SCIENCE-201801", "CS-SCIENCE-201802", "CS-SCIENCE-201901", "CS-SCIENCE-201902", "CS-SCIENCE-202001", "CS-SCIENCE-202002", "CS-SCIENCE-202101", "CS-SCIENCE-202102", "CS-SCIENCE-202201", "CS-SCIENCE-202202", "CS-SCIENCE-202301", "CS-SCIENCE-202302",
                    "IE-201801", "IE-201802", "IE-201901", "IE-201902", "IE-202001", "IE-202002", "IE-202101", "IE-202102", "IE-202201", "IE-202202", "IE-202301", "IE-202302",
                    "IE-SCIENCE-201801", "IE-SCIENCE-201802", "IE-SCIENCE-201901", "IE-SCIENCE-201902", "IE-SCIENCE-202001", "IE-SCIENCE-202002", "IE-SCIENCE-202101", "IE-SCIENCE-202102", "IE-SCIENCE-202201", "IE-SCIENCE-202202", "IE-SCIENCE-202301", "IE-SCIENCE-202302",
                    "MAT-201801", "MAT-201802", "MAT-201901", "MAT-201902", "MAT-202001", "MAT-202002", "MAT-202101", "MAT-202102", "MAT-202201", "MAT-202202", "MAT-202301", "MAT-202302","MAT-SCIENCE-201801", "MAT-SCIENCE-201802", "MAT-SCIENCE-201901", "MAT-SCIENCE-201902", "MAT-SCIENCE-202001", "MAT-SCIENCE-202002", "MAT-SCIENCE-202101", "MAT-SCIENCE-202102", "MAT-SCIENCE-202201", "MAT-SCIENCE-202202", "MAT-SCIENCE-202301", "MAT-SCIENCE-202302",
                    "EE-201801", "EE-201802", "EE-201901", "EE-201902", "EE-202001", "EE-202002", "EE-202101", "EE-202102", "EE-202201", "EE-202202", "EE-202301", "EE-202302",
                    "EE-SCIENCE-201801", "EE-SCIENCE-201802", "EE-SCIENCE-201901", "EE-SCIENCE-201902", "EE-SCIENCE-202001", "EE-SCIENCE-202002", "EE-SCIENCE-202101", "EE-SCIENCE-202102", "EE-SCIENCE-202201", "EE-SCIENCE-202202", "EE-SCIENCE-202301", "EE-SCIENCE-202302",
                    "ME-201801", "ME-201802", "ME-201901", "ME-201902", "ME-202001", "ME-202002", "ME-202101", "ME-202102", "ME-202201", "ME-202202", "ME-202301", "ME-202302",
                    "ME-SCIENCE-201801", "ME-SCIENCE-201802", "ME-SCIENCE-201901", "ME-SCIENCE-201902", "ME-SCIENCE-202001", "ME-SCIENCE-202002", "ME-SCIENCE-202101", "ME-SCIENCE-202102", "ME-SCIENCE-202201", "ME-SCIENCE-202202", "ME-SCIENCE-202301", "ME-SCIENCE-202302",
                    "BIO-201801", "BIO-201802", "BIO-201901", "BIO-201902", "BIO-202001", "BIO-202002", "BIO-202101", "BIO-202102", "BIO-202201", "BIO-202202", "BIO-202301", "BIO-202302",
                    "BIO-SCIENCE-201801", "BIO-SCIENCE-201802", "BIO-SCIENCE-201901", "BIO-SCIENCE-201902", "BIO-SCIENCE-202001", "BIO-SCIENCE-202002", "BIO-SCIENCE-202101", "BIO-SCIENCE-202102", "BIO-SCIENCE-202201", "BIO-SCIENCE-202202", "BIO-SCIENCE-202301", "BIO-SCIENCE-202302",
                    "PSY-201801", "PSY-201802", "PSY-201901", "PSY-201902", "PSY-202001", "PSY-202002", "PSY-202101", "PSY-202102", "PSY-202201", "PSY-202202", "PSY-202301", "PSY-202302",
                    "PSY-PHIL-201801", "PSY-PHIL-201802", "PSY-PHIL-201901", "PSY-PHIL-201902", "PSY-PHIL-202001", "PSY-PHIL-202002", "PSY-PHIL-202101", "PSY-PHIL-202102", "PSY-PHIL-202201", "PSY-PHIL-202202", "PSY-PHIL-202301", "PSY-PHIL-202302",
                    "MAN-201801", "MAN-201802","MAN-201901", "MAN-201902", "MAN-202001", "MAN-202002", "MAN-202101", "MAN-202102", "MAN-202201", "MAN-202202", "MAN-202301", 
                    "VACD-201801", "VACD-201802", "VACD-201901", "VACD-201902", "VACD-202001", "VACD-202002", "VACD-202101", "VACD-202102", "VACD-202201", "VACD-202202", "VACD-202301", "VACD-202302",
                    "ECON-201801", "ECON-201802", "ECON-201901", "ECON-201902", "ECON-202001", "ECON-202002", "ECON-202101", "ECON-202102", "ECON-202201", "ECON-202202", "ECON-202301", "ECON-202302"]
cs_sections = ["CS-201801", "CS-201802", "CS-201901", "CS-201902", "CS-202001", "CS-202002", "CS-202101", "CS-202102", "CS-202201", "CS-202202", "CS-202301", "CS-202302",
                    "CS-SCIENCE-201801", "CS-SCIENCE-201802", "CS-SCIENCE-201901", "CS-SCIENCE-201902", "CS-SCIENCE-202001", "CS-SCIENCE-202002", "CS-SCIENCE-202101", "CS-SCIENCE-202102", "CS-SCIENCE-202201", "CS-SCIENCE-202202", "CS-SCIENCE-202301", "CS-SCIENCE-202302"]

ie_sections = [ "IE-201801", "IE-201802", "IE-201901", "IE-201902", "IE-202001", "IE-202002", "IE-202101", "IE-202102", "IE-202201", "IE-202202", "IE-202301", "IE-202302",
                    "IE-SCIENCE-201801", "IE-SCIENCE-201802", "IE-SCIENCE-201901", "IE-SCIENCE-201902", "IE-SCIENCE-202001", "IE-SCIENCE-202002", "IE-SCIENCE-202101", "IE-SCIENCE-202102", "IE-SCIENCE-202201", "IE-SCIENCE-202202", "IE-SCIENCE-202301", "IE-SCIENCE-202302"]

mat_sections = [ "MAT-201801", "MAT-201802", "MAT-201901", "MAT-201902", "MAT-202001", "MAT-202002", "MAT-202101", "MAT-202102", "MAT-202201", "MAT-202202", "MAT-202301",   "MAT-202302","MAT-SCIENCE-201801", "MAT-SCIENCE-201802", "MAT-SCIENCE-201901", "MAT-SCIENCE-201902", "MAT-SCIENCE-202001", "MAT-SCIENCE-202002", "MAT-SCIENCE-202101", "MAT-SCIENCE-202102", "MAT-SCIENCE-202201", "MAT-SCIENCE-202202", "MAT-SCIENCE-202301", "MAT-SCIENCE-202302"]

ee_sections = [ "EE-201801", "EE-201802", "EE-201901", "EE-201902", "EE-202001", "EE-202002", "EE-202101", "EE-202102", "EE-202201", "EE-202202", "EE-202301", "EE-202302",
                    "EE-SCIENCE-201801", "EE-SCIENCE-201802", "EE-SCIENCE-201901", "EE-SCIENCE-201902", "EE-SCIENCE-202001", "EE-SCIENCE-202002", "EE-SCIENCE-202101", "EE-SCIENCE-202102", "EE-SCIENCE-202201", "EE-SCIENCE-202202", "EE-SCIENCE-202301", "EE-SCIENCE-202302"]

me_sections = [ "ME-201801", "ME-201802", "ME-201901", "ME-201902", "ME-202001", "ME-202002", "ME-202101", "ME-202102", "ME-202201", "ME-202202", "ME-202301", "ME-202302",
                    "ME-SCIENCE-201801", "ME-SCIENCE-201802", "ME-SCIENCE-201901", "ME-SCIENCE-201902", "ME-SCIENCE-202001", "ME-SCIENCE-202002", "ME-SCIENCE-202101", "ME-SCIENCE-202102", "ME-SCIENCE-202201", "ME-SCIENCE-202202", "ME-SCIENCE-202301", "ME-SCIENCE-202302"]

bio_sections = [ "BIO-201801", "BIO-201802", "BIO-201901", "BIO-201902", "BIO-202001", "BIO-202002", "BIO-202101", "BIO-202102", "BIO-202201", "BIO-202202", "BIO-202301","BIO-202302",
                    "BIO-SCIENCE-201801", "BIO-SCIENCE-201802", "BIO-SCIENCE-201901", "BIO-SCIENCE-201902", "BIO-SCIENCE-202001", "BIO-SCIENCE-202002", "BIO-SCIENCE-202101", "BIO-SCIENCE-202102", "BIO-SCIENCE-202201", "BIO-SCIENCE-202202", "BIO-SCIENCE-202301", "BIO-SCIENCE-202302"]

psy_sections = [ "PSY-201801", "PSY-201802", "PSY-201901", "PSY-201902", "PSY-202001", "PSY-202002", "PSY-202101", "PSY-202102", "PSY-202201", "PSY-202202", "PSY-202301", "PSY-202302",
                    "PSY-PHIL-201801", "PSY-PHIL-201802", "PSY-PHIL-201901", "PSY-PHIL-201902", "PSY-PHIL-202001", "PSY-PHIL-202002", "PSY-PHIL-202101", "PSY-PHIL-202102", "PSY-PHIL-202201", "PSY-PHIL-202202", "PSY-PHIL-202301"]

man_sections = ["MAN-201801", "MAN-201802","MAN-201901", "MAN-201902", "MAN-202001", "MAN-202002", "MAN-202101", "MAN-202102", "MAN-202201", "MAN-202202", "MAN-202301"]

vacd_sections = ["VACD-201801", "VACD-201802", "VACD-201901", "VACD-201902", "VACD-202001", "VACD-202002", "VACD-202101", "VACD-202102", "VACD-202201", "VACD-202202", "VACD-202301", "VACD-202302"]

econ_sections = ["ECON-201801", "ECON-201802", "ECON-201901", "ECON-201902", "ECON-202001", "ECON-202002", "ECON-202101", "ECON-202102", "ECON-202201", "ECON-202202", "ECON-202301", "ECON-202302"]

def extract_major_and_year(file_path):
    file_name = os.path.basename(file_path)
    parts = file_name.split('_')
    if len(parts) >= 2:
        major_code = parts[0][2:]  # Extract the major code, skipping the first two characters
        year = parts[1][:6]  # Extract the year (first 6 characters)
        return major_code, year
    else:
        return None, None


database = "SuGrad"
if client:
    for file_path in cs_file_paths:
        major_code, year = extract_major_and_year(file_path)
        print("Major Code: ", major_code)
        print("Year: ", year)
        collection_name = f"{major_code}-{year}"
        collection = create_collection(client, database, collection_name)
        if collection is not None:
            insert_courses(file_path, client, database, collection_name)

    for file_path in ie_file_paths:
        major_code, year = extract_major_and_year(file_path)
        print("Major Code: ", major_code)
        print("Year: ", year)
        collection_name = f"{major_code}-{year}"
        collection = create_collection(client, database, collection_name)
        if collection is not None:
            insert_courses(file_path, client, database, collection_name)

    for file_path in mat_file_paths:
        major_code, year = extract_major_and_year(file_path)
        print("Major Code: ", major_code)
        print("Year: ", year)
        collection_name = f"{major_code}-{year}"
        collection = create_collection(client, database, collection_name)
        if collection is not None:
            insert_courses(file_path, client, database, collection_name)

    for file_path in ee_file_paths:
        major_code, year = extract_major_and_year(file_path)
        print("Major Code: ", major_code)
        print("Year: ", year)
        collection_name = f"{major_code}-{year}"
        collection = create_collection(client, database, collection_name)
        if collection is not None:
            insert_courses(file_path, client, database, collection_name)

    for file_path in me_file_paths:
        major_code, year = extract_major_and_year(file_path)
        print("Major Code: ", major_code)
        print("Year: ", year)
        collection_name = f"{major_code}-{year}"
        collection = create_collection(client, database, collection_name)
        if collection is not None:
            insert_courses(file_path, client, database, collection_name)
    
    for file_path in bio_file_paths:
        major_code, year = extract_major_and_year(file_path)
        print("Major Code: ", major_code)
        print("Year: ", year)
        collection_name = f"{major_code}-{year}"
        collection = create_collection(client, database, collection_name)
        if collection is not None:
            insert_courses(file_path, client, database, collection_name)

    for file_path in psy_file_paths:
         major_code, year = extract_major_and_year(file_path)
         print("Major Code: ", major_code)
         print("Year: ", year)
         collection_name = f"{major_code}-{year}"
         collection = create_collection(client, database, collection_name)
         if collection is not None:
             insert_courses(file_path, client, database, collection_name)
    

    for file_path in man_file_paths:
        major_code, year = extract_major_and_year(file_path)
        print("Major Code: ", major_code)
        print("Year: ", year)
        collection_name = f"{major_code}-{year}"
        collection = create_collection(client, database, collection_name)
        if collection is not None:
            insert_courses(file_path, client, database, collection_name)

    for file_path in econ_file_paths:
        major_code, year = extract_major_and_year(file_path)
        print("Major Code: ", major_code)
        print("Year: ", year)
        collection_name = f"{major_code}-{year}"
        collection = create_collection(client, database, collection_name)
        if collection is not None:
            insert_courses(file_path, client, database, collection_name)

    for file_path in vacd_file_paths:
        major_code, year = extract_major_and_year(file_path)
        print("Major Code: ", major_code)
        print("Year: ", year)
        collection_name = f"{major_code}-{year}"
        collection = create_collection(client, database, collection_name)
        if collection is not None:
            insert_courses(file_path, client, database, collection_name)


client.close()