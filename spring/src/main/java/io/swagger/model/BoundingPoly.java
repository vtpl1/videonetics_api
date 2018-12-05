package io.swagger.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import io.swagger.model.Vertex;
import java.util.ArrayList;
import java.util.List;
import org.springframework.validation.annotation.Validated;
import javax.validation.Valid;
import javax.validation.constraints.*;

/**
 * BoundingPoly
 */
@Validated
@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2018-12-05T07:09:15.776Z[GMT]")

public class BoundingPoly   {
  @JsonProperty("vertices")
  @Valid
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
  @ApiModelProperty(value = "")

  @Valid

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
    return Objects.hash(vertices);
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

