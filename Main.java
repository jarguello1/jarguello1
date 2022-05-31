package com.josearguello;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;



public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        ArrayList<Integer> clipLengthList = new ArrayList<>();
        ArrayList<Integer> clipQtyList = new ArrayList<>();
        List<Integer> totalClipQty = new ArrayList<>();


        while (true) {
            System.out.println("Clip Length: ");
            int clipLength = scanner.nextInt();
            clipLengthList.add(clipLength);

            System.out.println("How many clips are " + clipLength + "?");
            int clipQty = scanner.nextInt();
            clipQtyList.add(clipQty);

            for (int i = 0; i < clipQtyList.size(); i++) {
                System.out.println(clipLengthList.get(i) + "mm " + clipQtyList.get(i));
            }
            System.out.println();
            System.out.println("Enter 1 to calculate values.\n" +
                               "Enter 2 to delete values\n" +
                               "Enter any other number to continue adding values");


            int input = scanner.nextInt();
            if (input == 1) {
                System.out.println("Clip Amounts: " + clipLengthList);
                System.out.println("# of Panels: " + sum(clipQtyList));
                for (int i = 0; i < clipQtyList.size(); i++) {
                    int num1 = clipQtyList.get(i);
                    int num2 = clipLengthList.get(i);
                    totalClipQty.add(num2 * num1);
                }
                System.out.println(sum(totalClipQty) + "mm");
                break;
            }
            else if (input == 2) {
                System.out.println("Delete which entry? ");
                int delInput = scanner.nextInt();
                System.out.println("Deleted: Size: " + clipLengthList.get(delInput - 1)
                                   + "\nQty: " + clipQtyList.get(delInput - 1));
                clipLengthList.remove(delInput - 1);
                clipQtyList.remove(delInput - 1);
            }
        }
    }
    public static int sum(List<Integer> list)
    {
        // create a stream of integers
        // add the integers
        return list.stream()
                .mapToInt(i -> i)
                .sum();
    }
}

