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
import io.swagger.client.model.Vertex;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * BoundingPoly
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2018-12-05T14:46:13.659Z[GMT]")public class BoundingPoly {

  @SerializedName("vertices")
  private List<Vertex> vertices = null;
  public BoundingPoly vertices(List<Vertex> vertices) {
    this.vertices = vertices;
    return this;
  }

  public BoundingPoly addVerticesItem(Vertex verticesItem) {
    if (this.vertices == null) {
      this.vertices = new ArrayList<Vertex>();
    }
    this.vertices.add(verticesItem);
    return this;
  }

  /**
  * Get vertices
  * @return vertices
  **/
  @Schema(description = "")
  public List<Vertex> getVertices() {
    return vertices;
  }
  public void setVertices(List<Vertex> vertices) {
    this.vertices = vertices;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BoundingPoly boundingPoly = (BoundingPoly) o;
    return Objects.equals(this.vertices, boundingPoly.vertices);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(vertices);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BoundingPoly {\n");
    
    sb.append("    vertices: ").append(toIndentedString(vertices)).append("\n");
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