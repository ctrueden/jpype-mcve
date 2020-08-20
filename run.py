# Python-side imports.
import jpype
import jpype.imports
from jpype import JClass

# Start Java.
jpype.startJVM(classpath=['.'])

# Java-side imports.
from java.lang import Class

def importWorkaround(javaClassName):
    javaSideClass = Class.forName(javaClassName)
    return JClass(javaSideClass)

# Print out the class path.
from java.lang import System
classpath = System.getProperty('java.class.path')
print(f'Class path = {classpath}')

# Load the class.
MyClass = importWorkaround('com.mystuff.MyClass')

# Create an instance of the class.
thing = MyClass()

# Execute the method!
thing.doStuff()
