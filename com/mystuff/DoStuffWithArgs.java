package com.mystuff;
public interface DoStuffWithArgs {
  default void doStuff(String arg) {
    System.out.println("doStuff(\"" + arg + "\")");
  }
}
