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
import java.math.BigDecimal;

/**
 * VertexWithValue
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2018-12-06T15:32:55.264Z[GMT]")public class VertexWithValue {

  @SerializedName("value")
  private BigDecimal value = null;

  @SerializedName("vertex")
  private Vertex vertex = null;
  public VertexWithValue value(BigDecimal value) {
    this.value = value;
    return this;
  }

  

  /**
  * Get value
  * @return value
  **/
  @Schema(example = "5", description = "")
  public BigDecimal getValue() {
    return value;
  }
  public void setValue(BigDecimal value) {
    this.value = value;
  }
  public VertexWithValue vertex(Vertex vertex) {
    this.vertex = vertex;
    return this;
  }

  

  /**
  * Get vertex
  * @return vertex
  **/
  @Schema(description = "")
  public Vertex getVertex() {
    return vertex;
  }
  public void setVertex(Vertex vertex) {
    this.vertex = vertex;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    VertexWithValue vertexWithValue = (VertexWithValue) o;
    return Objects.equals(this.value, vertexWithValue.value) &&
        Objects.equals(this.vertex, vertexWithValue.vertex);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(value, vertex);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class VertexWithValue {\n");
    
    sb.append("    value: ").append(toIndentedString(value)).append("\n");
    sb.append("    vertex: ").append(toIndentedString(vertex)).append("\n");
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
