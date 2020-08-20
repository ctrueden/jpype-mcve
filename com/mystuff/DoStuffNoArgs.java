package com.mystuff;
public interface DoStuffNoArgs {
  default void doStuff() {
    System.out.println("doStuff()");
  }
}
