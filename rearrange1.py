{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red24\green24\blue24;\red255\green255\blue255;}
{\*\expandedcolortbl;;\cssrgb\c12157\c12157\c12157;\cssrgb\c100000\c100000\c100000;}
\margl1440\margr1440\vieww20180\viewh11600\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
import re\
def rearrange_name(name):\
\'a0\'a0\'a0\'a0result = re.search(r"^([\\w .]*), ([\\w .]*)$", name)\
\'a0\'a0\'a0\'a0if result == None:\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0return name\
\'a0\'a0\'a0\'a0return "\{\} \{\}".format(result[2], result[1])\
\
}