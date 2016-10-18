import os
from pathlib import Path
import re
import sys

def printHeader():
    outputFile.write("""<?xml version="1.0" encoding="UTF-8"?>
<quiz>
<!-- question: 0  -->
  <question type="category">
    <category>
        <text>$course$/CodeRunner Test</text>

    </category>
  </question>
  """)
def printFooter():
    outputFile.write("\n</quiz>")

def printTask(task):
    outputFile.write("""<question type="coderunner">
    <name>
      <text>{0}</text>
    </name>
    """.format(task))

    outputFile.write("<questiontext format=\"html\"><text><![CDATA[")
    outputFile.write(Path(task+"/statement.html").read_text().replace("<span class=\"tex-span\">","").replace("</span>",""))
    outputFile.write("""]]></text>
    </questiontext>
    <generalfeedback format="html">
      <text></text>
    </generalfeedback>
    <defaultgrade>1.0000000</defaultgrade>
    <penalty>0.3333333</penalty>
    <hidden>0</hidden>
    <coderunnertype>java_program</coderunnertype>
    <prototypetype>0</prototypetype>
    <allornothing>1</allornothing>
    <penaltyregime>0,0,5,10,...</penaltyregime>
    <showsource>0</showsource>
    <answerboxlines>18</answerboxlines>
    <answerboxcolumns>100</answerboxcolumns>
    <useace>1</useace>
    <resultcolumns></resultcolumns>
    <answer></answer>
    <combinatortemplate></combinatortemplate>
    <testsplitterre></testsplitterre>
    <enablecombinator></enablecombinator>
    <pertesttemplate></pertesttemplate>
    <language></language>
    <acelang></acelang>
    <sandbox></sandbox>
    <grader></grader>
    <cputimelimitsecs></cputimelimitsecs>
    <memlimitmb></memlimitmb>
    <sandboxparams></sandboxparams>
    <templateparams></templateparams>

    <testcases>
    """)
    tests = next(os.walk('./' + task + "/tests/"))[2]
    i = 0
    for test in tests:
        if re.match("^[0-9]+$", test) is None:
            continue
        outputFile.write("""<testcase useasexample="{0}" hiderestiffail="1" mark="1.0000000" >
      <testcode>
                <text></text>
      </testcode>
      <stdin>
                <text>{1}</text>
      </stdin>
      <expected>
                <text>{2}</text>
      </expected>
      <extra>
                <text></text>
      </extra>
      <display>
                <text>HIDE</text>
      </display>
    </testcase>
     """.format(1 if i < 2 else 0, Path(task + "/tests/" + test).read_text(), Path(task + "/tests/" + test + ".a").read_text()));
        i += 1;
    outputFile.write("""</testcases>
 </question>""") 

                  
def printAllTasks():
    tasks = next(os.walk('.'))[1]
    for task in tasks:
        printTask (task);

outputFile = open("questions.xml", "w");
printHeader()
printAllTasks()
printFooter()
outputFile.close()


