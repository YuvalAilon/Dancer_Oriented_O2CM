package com.O2CMPlus.DataScraping;

import org.jsoup.nodes.Element;

public class EventRaw {

    String name;
    String heatID;
    String competitionID;

    public EventRaw(Element eventLink, String competitionID) {
        name = eventLink.text();
        heatID = HelperFunctions.extractID(
                eventLink.attr("href"),
                "heatid=",
                '&'
        );
        this.competitionID = competitionID;
    }

    @Override
    public String toString() {
        return heatID + "\t| " + getLink() + "\t| " + name;
    }

    public String getLink(){
        return "scoresheet3.asp?event="  + competitionID + "&heatid=" + heatID;
    }
}
