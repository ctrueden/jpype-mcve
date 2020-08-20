package com.mystuff;
public interface Interface1 {
  default void doStuff() {
    System.out.println("doStuff()");
  }
}
