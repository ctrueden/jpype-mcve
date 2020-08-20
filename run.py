import jpype
import jpype.imports

jpype.startJVM(classpath=['myJar.jar'])

from com.mystuff import MyClass

thing = MyClass()
thing.doStuff()
