# -*- coding: cp1252 -*-
import csv

projects = []
unicode_projects = []
list_techniques = []
def init():
    global projects
    projects = csv.DictReader(open("data.csv"))   

    for dicts in projects:
        temp_dict = {} 
        for value in dicts:
            if value.find("no") != -1 and dicts[value].isdigit():
                temp_dict[unicode(value, "utf-8")] = int(dicts[value])
            else:
                temp_dict[unicode(value, "utf-8")] = unicode(dicts[value], "utf-8")
        unicode_projects.append(temp_dict)
    
    for dicts in unicode_projects:
        temp = dicts['techniques_used'].split(',')
	list_techniques = temp
	for i in temp:
	    if i not in list_techniques and len(i) > 0:
		list_techniques.append(i)
	    temp2 = dicts['techniques_used']
	    if len(temp2) < 1:
		list_techniques.remove(temp2)
        list_techniques.sort()
        dicts['techniques_used'] = list_techniques
        errcode = 0

    return unicode_projects


def project_count():   
    if len(unicode_projects) == 0:
	errcode = 1
        return (errcode, len(unicode_projects))
    else:
	errcode = 0
        return (errcode, len(unicode_projects))

def lookup_project(id):
    if len(unicode_projects) == 0:
        print "LADDA INIT() FÖRST DUMBASS!"
    elif id > len(unicode_projects):
	errcode = 2
	return errcode, None
    else:
        for dicts in unicode_projects:
            if dicts['project_no'] == int(id):
		errcode = 0
                return errcode, dicts


def retrieve_techniques():
    dict_tec_lista = []
    for dicts in unicode_projects:
	temp = dicts['techniques_used']
	for i in temp:
	    if i not in dict_tec_lista and len(i) > 0:
		dict_tec_lista.append(i)
    dict_tec_lista.sort()
    errcode = 0
    return errcode, dict_tec_lista


def retrieve_projects(sort_by='start_date', sort_order='asc', techniques=None, search=None, search_fields=None):
    return_lista = []
    
    for proj in unicode_projects:
        add = False
        
        if search or search_fields:
            for field in search_fields:
                data = proj[field]
                if isinstance(data, int):
                    data = str(data)

                if data.lower().find(unicode(search, 'utf-8').lower()) != -1:
                    add = True
        else:
            add = True

        if add and techniques:
            for tech in techniques:
                if not tech in proj['techniques_used']:
                    add = False
                    continue

        if add:
            return_lista.append(proj)

    return_lista.sort(key=lambda val: val[sort_by])
    
    if sort_order == 'desc':
        return_lista.reverse()

    errcode = 0
    return errcode, return_lista


def retrieve_technique_stats():
    temp_dict = {}
    proj_dict = {}
    temp_list = []
    asd_dict = {}
    dsa_list = []
    
    for tech in retrieve_techniques()[1]:
        x = 0
        temp_list = []
        temp_dict = {'name': str(tech)}
        
        for dicts in unicode_projects:
            if tech in dicts['techniques_used']:
                x += 1
                asd_dict['id'] = dicts['project_no']
                asd_dict['name'] = dicts['project_name']
                temp_list.append(asd_dict)
                asd_dict = {}
        temp_dict['count'] = x

        temp_list = sorted(temp_list, key=lambda asd_dict: asd_dict['name'])

        temp_dict['projects'] = temp_list
        dsa_list.append(temp_dict)
    errcode = 0
    return errcode, dsa_list
        
    


