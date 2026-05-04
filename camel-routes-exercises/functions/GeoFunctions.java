package com.cefriel.tutorial;

import com.cefriel.template.utils.TemplateFunctions;

public class GeoFunctions extends TemplateFunctions {
    public String getLat(String position) {
        if (position == null || !position.startsWith("Point(")) return null;
        String coords = position.substring(6, position.length() - 1);
        String[] parts = coords.split(" ");
        if (parts.length != 2) return null;
        return parts[1];
    }
    public String getLong(String position) {
        if (position == null || !position.startsWith("Point(")) return null;
        String coords = position.substring(6, position.length() - 1);
        String[] parts = coords.split(" ");
        if (parts.length != 2) return null;
        return parts[0];
    }
}
