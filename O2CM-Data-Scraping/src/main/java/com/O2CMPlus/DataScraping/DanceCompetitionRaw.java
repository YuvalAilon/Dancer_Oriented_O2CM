package com.O2CMPlus.DataScraping;

import jdk.jfr.Event;
import org.jsoup.Connection;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;
import java.sql.Array;
import java.util.*;

public class DanceCompetitionRaw {
    String name;
    String ID;

    public static String toStringSeparator = "\t, ";

    public DanceCompetitionRaw(Element eventLink) {
        name = eventLink.text();
        String linkText = eventLink.attr("href");
        ID = HelperFunctions.extractID(
            linkText,
            "event=",
            '&'
        );
    }

    public DanceCompetitionRaw(String toString) {
        String[] separated = toString.split(toStringSeparator);
        System.out.println(Arrays.toString(separated));
        name = separated[2];
        ID   = separated[0];
    }

    @Override
    public String toString() {
        return  ID + toStringSeparator + getLink() + toStringSeparator + name;
    }

    public ArrayList<EventRaw> generateEvents(){
        ArrayList<EventRaw> events = new ArrayList<EventRaw>();
        try {
            Document competition = Jsoup.connect("https://results.o2cm.com/"+getLink())
                .data("selDiv", "")
                .data("selAge", "")
                .data("selSkl", "")
                .data("selSty", "")
                .data("selEnt", "")
                .data("submit", "OK")
                .data("event" ,       ID)
                .post();
            Elements links = competition.select("a[href]");
            for (Element link : links) {
                String linkText = link.attr("href");
                if(linkText.contains("scoresheet") && linkText.contains("asp")){
                    EventRaw temp = new EventRaw(link, ID);
                    System.out.println(temp);
                }
            }

        }catch (IOException e){
            System.out.println("Could not access " + name  );
            System.out.println(e.toString());
        }
        return null;
    }

    public String getLink(){
        return "event3.asp?event=" + ID;
    }
}
