package com.O2CMPlus.DataScraping;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class HelperFunctions {
    public static String extractID(String link, String eventIDStart,char eventIDEnd){
        StringBuilder id = new StringBuilder();
        int idIndex = link.indexOf(eventIDStart) + eventIDStart.length();
        while(idIndex < link.length() && link.charAt(idIndex) != eventIDEnd){
            id.append(link.charAt(idIndex));
            idIndex += 1;
        }
        return id.toString();
    }

    public static void writeFile(String filepath, String contents) throws IOException {
        FileWriter fileWriter = new FileWriter(filepath);

        for (int index = 0; index < contents.length(); index++) {
            fileWriter.write(contents.charAt(index));
        }

        fileWriter.close();
    }

    public static String readFile(String filepath) throws IOException {
        int chararcter;
        StringBuilder contents = new StringBuilder();
        FileReader fileReader = null;
        try{
            fileReader = new FileReader(filepath);
        }catch (FileNotFoundException e){
            System.out.println("File not Found :(");
        }

        while ((chararcter=fileReader.read())!=-1)
            contents.append((char)chararcter);

        return contents.toString();
    }

}
