/*
 * Videonetics Visual Computing Platform
 * API to access the Videonetics Visual Computing Platform for analytics events
 *
 * OpenAPI spec version: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package io.swagger.client.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;

/**
 * Location
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2018-12-05T14:46:16.991Z[GMT]")public class Location {

  @SerializedName("lat")
  private Float lat = null;

  @SerializedName("long")
  private Float _long = null;
  public Location lat(Float lat) {
    this.lat = lat;
    return this;
  }

  

  /**
  * Get lat
  * @return lat
  **/
  @Schema(example = "22.572645", description = "")
  public Float getLat() {
    return lat;
  }
  public void setLat(Float lat) {
    this.lat = lat;
  }
  public Location _long(Float _long) {
    this._long = _long;
    return this;
  }

  

  /**
  * Get _long
  * @return _long
  **/
  @Schema(example = "88.363892", description = "")
  public Float getLong() {
    return _long;
  }
  public void setLong(Float _long) {
    this._long = _long;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Location location = (Location) o;
    return Objects.equals(this.lat, location.lat) &&
        Objects.equals(this._long, location._long);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(lat, _long);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Location {\n");
    
    sb.append("    lat: ").append(toIndentedString(lat)).append("\n");
    sb.append("    _long: ").append(toIndentedString(_long)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}
