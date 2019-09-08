package geoLocation;

public class GePoint {
    private double latitude; // Î³¶È×ø±ê
    private double longtitude; // ¾­¶È×ø±ê
public GePoint() {
}
public GePoint(double latitude, double longtitude) {
    this.latitude = latitude;
    this.longtitude = longtitude;
}
public double getLatitude() {
    return 2 * latitude * Math.PI / 360 ;
}
public void setLatitude(double latitude) {
    this.latitude = latitude;
}
public double getLongtitude() {
    return 2 * longtitude * Math.PI / 360;
}
public void setLongtitude(double longtitude) {
        this.longtitude = longtitude;
    }
}
