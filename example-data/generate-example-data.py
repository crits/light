#!/usr/bin/env python3
import json
#
# This is a simple python script that generates a JSON document which is used
# to represent the cyber intelligence data contained within the McAfee Intelligence
# report entitled:
# * "Malicious Document Targets Pyeongchang Olympics"
#
# A copy of this is available here:
# * https://www.threatminer.org/_reports/2018/Malicious%20Document%20Targets%20Pyeongchang%20Olympics%20_%20McAfee%20Blogs.pdf
#

report_sourcename = "McAfee OSINT"
report_refname = "https://securingtomorrow.mcafee.com/mcafee-labs/malicious-document-targets-pyeongchang-olympics/"
report_permanent_archive = "https://www.threatminer.org/_reports/2018/Malicious%20Document%20Targets%20Pyeongchang%20Olympics%20_%20McAfee%20Blogs.pdf"

# All of these things are coming from a common source, so let us define a "source Access" object
# to work from
mcafee_osint_source_access = {
        'name': report_sourcename, # Use the name I defined earlier, continue to use this an FK
        'default_tlp': 'white',    # By default, this will be TLP:WHITE to any roles the source is
                                   # extended to.
        'active': True             # Set this as active (deactivation flag so we can preserve "old" sources)
}

# I'm just gonna use numeric Ids below for the sake of brevity, but these could easily be translated to stringified BSON ObjectId
# values if desired, to support the GUID concept
observables = [
        {'value': '농식품부, 평창 동계올림픽 대비 축산악취 방지대책 관련기관 회의 개최.doc',
         'observation_type': 'file-name',
         'id': 1},
        {'value': 'Organized by Ministry of Agriculture and Forestry and Pyeongchang Winter Olympics.doc',
         'observation_type': 'file-name',
         'id': 2},
        {'value': '43.249.39.152',
         'observation_type': 'ipv4-addr',
         'id': 3},
        {'value': 'info@nctc.go.kr',
         'observation_type': 'email-addr',
         'id': 4},
        {'value': 'ospf1-apac-sg.stickyadstv.com',
         'observation_type': 'domain-name',
         'id': 5},
        {'value': 'https://www.thlsystems.forfirst.cz/images/adv_s3.png',
         'observation_type': 'url',
         'id': 6},
        {'value': '/images/adv_s3.png',
         'observation_type': 'url',
         'id': 7},
        {'value': 'adv_s3.png',
         'observation_type': 'url',
         'id': 8},
        {'value': 'adv_s3.png',
         'observation_type': 'file-name',
         'id': 9},
        {'value': 'www.thlsystems.forfirst.cz',
         'observation_type': 'domain-name',
         'id': 10},
        {'value': '&&set  xmd=echo  iex (ls env:tjdm).value ^| powershell -noni  -noex  -execut bypass -noprofile  -wind  hidden     – && cmd   /C%xmd%',
         'observation_type': 'artifact',
         'observation_subtype': 'string-cmd',
         'id': 11},
        {'value': 'https://www.thlsystems.forfirst.cz:443/components/com_tags/views/login/process.php',
         'observation_type': 'url',
         'id': 12},
        {'value': 'https://www.thlsystems.forfirst.cz/components/com_tags/views/login/process.php',
         'observation_type': 'url',
         'id': 13},
        {'value': '/components/com_tags/views/login/process.php',
         'observation_type': 'url',
         'id': 14},
        {'value': '/com_tags/views/login/process.php',
         'observation_type': 'url',
         'id': 15},
        {'value': 'https://200.122.181.63:443/components/com_tags/views/news.php',
         'observation_type': 'url',
         'id': 16},
        {'value': '/components/com_tags/views/news.php',
         'observation_type': 'url',
         'id': 17},
        {'value': '/components/com_tags/',
         'observation_type': 'url',
         'id': 18},
        {'value': '200.122.181.63',
         'observation_type': 'ipv4-addr',
         'id': 19},
        {'value': 'C:\\Windows\\system32\\schtasks.exe” /Create /F /SC DAILY /ST 14:00 /TN “MS Remoute Update” /TR C:\\Users\\Ops03\\AppData\\Local\\view.hta',
         'observation_type': 'artifact',
         'observation_subtype': 'string-cmd',
         'id': 20},
        {'value': 'C:\\Users\\Ops03\\AppData\\Local\\view.hta',
         'observation_type': 'file-path',
         'id': 21},
        {'value': '%AppData%\\Local\\view.hta',
         'observation_type': 'file-path',
         'id': 22},
        {'value': 'view.hta',
         'observation_type': 'file-name',
         'id': 23},
        {'value': '81.31.47.101',
         'observation_type': 'ipv4-addr',
         'id': 24},
        {'value': 'thlsystems.forfirst.cz',
         'observation_type': 'domain-name',
         'id': 25},
        {'value': 'https://www.thlsystems.forfirst.cz/components/com_tags/views/admin/get.php',
         'observation_type': 'url',
         'id': 26},
        {'value': '/components/com_tags/views/admin/get.php',
         'observation_type': 'url',
         'id': 27},
        {'value': 'mafra.go.kr.jeojang.ga',
         'observation_type': 'domain-name',
         'id': 28},
        {'value': '위험 경보 (전국야생조류 분변 고병원성 AI(H5N6형) 검출).docx',
         'observation_type': 'file-name',
         'id': 29},
        {'value': 'c388b693d10e2b84af52ab2c29eb9328e47c3c16',
         'observation_type': 'file-sha1',
         'id': 30},
        {'value': '8ad0a56e3db1e2cd730031bdcae2dbba3f7aba9c',
         'observation_type': 'file-sha1',
         'id': 31},
]

targets = [
        {'id': 32,
         'target_email': 'icehockey@pyeongchang2018.com',
         'target_name': 'Ice Hockey'}
]

events = [
        {'id': 33,
         'event_start': '2017-12-22T00:00:00.000Z',
         'event_end': '2017-12-28T00:00:00.000Z',
         'event_reported': '2018-01-06T00:00:00.000Z',
         'event_threat': 'Phishing',
         'event_type': 'Blog Post',
         'event_title': 'Malicious Document Targets Pyeongchang Olympics',
        }
]

# In general, I try to make relationships adhere to the following English convention:
#   {from} was {rel_type} {to}
#
relationships = [
        {'from': 1,
         'to': 31,
         'rel_type': 'Related To'}, # Opp = Related To
        {'from': 29,
         'to': 30,
         'rel_type': 'Related To'}, # Opp = Related To
        {'from': 2,
         'to': 1,
         'rel_type': 'Translated From'}, # Opp = Translated From
        {'from': 31,
         'to': 32,   # Note that this is referring to the one "target" reported
         'rel_type': 'Received By'}, # Opp = Received
        {'from': 31,
         'to': 3,
         'rel_type': 'Sent From'}, # Opp = Sent
        {'from': 31,
         'to': 4,
         'rel_type': 'Sent From'}, # Opp = Sent
        {'from': 31,
         'to': 5,
         'rel_type': 'Sent From'}, # Opp = Sent
        {'from': 31,
         'to': 6,
         'rel_type': 'Contacted'}, # Opp = Contacted From
        {'from': 6,
         'to': 7,
         'rel_type': 'Derived'},   # Opp = Derived From
        {'from': 6,
         'to': 8,
         'rel_type': 'Derived'},   # Opp = Derived From
        {'from': 8,
         'to': 9,
         'rel_type': 'Derived'},   # Opp = Derived From
        {'from': 6,
         'to': 10,
         'rel_type': 'Derived'},   # Opp = Derived From
        {'from': 9,
         'to': 11,
         'rel_type': 'Executed'},   # Opp = Executed By
        {'from': 9,
         'to': 12,
         'rel_type': 'Contacted'},   # Opp = Contacted From
        {'from': 12,
         'to': 13,
         'rel_type': 'Derived'},   # Opp = Derived From
        {'from': 12,
         'to': 14,
         'rel_type': 'Derived'},   # Opp = Derived From
        {'from': 12,
         'to': 15,
         'rel_type': 'Derived'},   # Opp = Derived From
        {'from': 12,
         'to': 10,
         'rel_type': 'Derived'},   # Opp = Derived From
        {'from': 13,
         'to': 14,
         'rel_type': 'Derived'},   # Opp = Derived From
        {'from': 13,
         'to': 15,
         'rel_type': 'Derived'},   # Opp = Derived From
        {'from': 13,
         'to': 10,
         'rel_type': 'Derived'},   # Opp = Derived From
        {'from': 9,
         'to': 21,
         'rel_type': 'Wrote'},   # Opp = Written By
        {'from': 21,
         'to': 16,
         'rel_type': 'Contacted'},   # Opp = Contacted From
        {'from': 16,
         'to': 17,
         'rel_type': 'Derived'},   # Opp = Derived From
        {'from': 16,
         'to': 18,
         'rel_type': 'Derived'},   # Opp = Derived From
        {'from': 16,
         'to': 19,
         'rel_type': 'Derived'},   # Opp = Derived From
        {'from': 20,
         'to': 9,
         'rel_type': 'Executed By'},   # Opp = Executed
        {'from': 21,
         'to': 22,
         'rel_type': 'Derived'},   # Opp = Derived From
        {'from': 21,
         'to': 23,
         'rel_type': 'Derived'},   # Opp = Derived From
        {'from': 10,
         'to': 25,
         'rel_type': 'Subdomain Of'},   # Opp = Superdomain Of
        {'from': 25,
         'to': 24,
         'rel_type': 'Resolved To'},   # Opp = Resolved From
        {'from': 21,
         'to': 26,
         'rel_type': 'Contacted'},   # Opp = Contacted From
        {'from': 26,
         'to': 27,
         'rel_type': 'Derived'},   # Opp = Derived From
        {'from': 19,
         'to': 28,
         'rel_type': 'Resolved From'},   # Opp = Resolved To
        {'from': 33,
         'to': 32,
         'rel_type': 'Reported'}, # Opp = Reported By
]

# Forge a relationship between all observables and the Event. There's probably some
# argument to be had about handling "Derived" objects. My opinion is that you choose
# to do it arbitrarily in the way that makes sense to you. Just be consistent internally.
for o in observables:
    relationships.append({'from': 33, 'to': o['id'], 'rel_type': 'Reported'})

# Finally, add source/reference/tlp information to every thing that's a real TLO. Again,
# be consistent internally about what constitutes a "Source" but don't set any hard
# expectations around this.
for collection in [observables, targets, events]:
    for o in collection:
        o['source'] = []
        o['source'].append({'name': mcafee_osint_source_access['name'],
                            'tlp': mcafee_osint_source_access['default_tlp'],
                            'instances': []})
        o['source'][-1]['instances'].append({'reference': report_refname, 'method': 'blog post'})
        o['source'][-1]['instances'].append({'reference': report_permanent_archive, 'method': 'APTnotes archive'})

# Figure I'd just dump it to stdout
print(json.dumps({'observables': observables, 'relationships': relationships, 'targets': targets, 'events': events}))
