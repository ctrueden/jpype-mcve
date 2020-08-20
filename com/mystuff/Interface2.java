package com.mystuff;
public interface Interface2 {
  default void doStuff(String arg) {
    System.out.println("doStuff(String)");
  }
}
