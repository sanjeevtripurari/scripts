#!/usr/bin/env python 

who = 'wesley@python.is.cool'
body = '''\
From: %(who)s
To: %(who)s
Subject: test msg

Hello World!
''' % {'who': who}

print body
