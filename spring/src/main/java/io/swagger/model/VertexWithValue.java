package io.swagger.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import io.swagger.model.Vertex;
import java.math.BigDecimal;
import org.springframework.validation.annotation.Validated;
import javax.validation.Valid;
import javax.validation.constraints.*;

/**
 * VertexWithValue
 */
@Validated
@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2018-12-05T07:09:15.776Z[GMT]")

public class VertexWithValue   {
  @JsonProperty("value")
  private BigDecimal value = null;

  @JsonProperty("vertex")
  private Vertex vertex = null;

  public VertexWithValue value(BigDecimal value) {
    this.value = value;
    return this;
  }

  /**
   * Get value
   * @return value
  **/
  @ApiModelProperty(example = "5", value = "")

  @Valid

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
  @ApiModelProperty(value = "")

  @Valid

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
    return Objects.hash(value, vertex);
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

