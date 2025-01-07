package com.O2CMPlus.DataScraping;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;
import java.io.File;
import java.io.FileReader;
import java.util.ArrayList;

/**
 * Hello world!
 */
public class App {
    public static void main(String[] args) {
        //updateCompetitionLinks("CompetitionList.txt");

       DanceCompetitionRaw terrier = new DanceCompetitionRaw("tub24\t, event3.asp?event=tub24\t, Tufts University Ballroom Competition");
       terrier.generateEvents();
    }

    /**
     *
     * @param filepath path of the file of competition links to update
     * @return Whether the file was updated
     */
    public static Boolean updateCompetitionLinks(String filepath) {
        Elements links = new Elements();
        try {
            Document O2CM = Jsoup.connect("https://results.o2cm.com/").get();
            links = O2CM.select("a[href]");
            System.out.println("Reached O2CM main page :)");
        }catch (IOException e){
            System.out.print("O2CM can't be reached right now :(");
            return false;
        }

        StringBuilder competitionList = new StringBuilder();
        for (Element link : links){
            DanceCompetitionRaw currentComp = new DanceCompetitionRaw(link);
            competitionList.append(currentComp);
            competitionList.append("\n");
        }

        try{
            HelperFunctions.writeFile(filepath,competitionList.toString());
            return true;
        }catch (IOException e){
            System.out.print("Couldn't Write File :/");
            return false;
        }
    }


    public static void getO2CMMainPageTest(){
        try {
            Document O2CM = Jsoup.connect("https://results.o2cm.com/").get();
            Elements links = O2CM.select("a[href]");
            System.out.println("Reached O2CM main page :)");
            for (int i = 0; i < 10; i++){
                DanceCompetitionRaw temp = new DanceCompetitionRaw(links.get(i));

            }

        }catch (IOException e){
            System.out.print("O2CM can't be reached right now :(");
        }
    }
}
