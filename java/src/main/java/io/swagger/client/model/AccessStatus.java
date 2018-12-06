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
 * AccessStatus
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2018-12-06T03:19:41.434Z[GMT]")public class AccessStatus {

  @SerializedName("createdOn")
  private Long createdOn = null;

  @SerializedName("lastAccesseOn")
  private Long lastAccesseOn = null;

  @SerializedName("firstAccesseOn")
  private Long firstAccesseOn = null;

  @SerializedName("onlineTimeInSec")
  private Float onlineTimeInSec = null;
  public AccessStatus createdOn(Long createdOn) {
    this.createdOn = createdOn;
    return this;
  }

  

  /**
  * Get createdOn
  * @return createdOn
  **/
  @Schema(description = "")
  public Long getCreatedOn() {
    return createdOn;
  }
  public void setCreatedOn(Long createdOn) {
    this.createdOn = createdOn;
  }
  public AccessStatus lastAccesseOn(Long lastAccesseOn) {
    this.lastAccesseOn = lastAccesseOn;
    return this;
  }

  

  /**
  * Get lastAccesseOn
  * @return lastAccesseOn
  **/
  @Schema(description = "")
  public Long getLastAccesseOn() {
    return lastAccesseOn;
  }
  public void setLastAccesseOn(Long lastAccesseOn) {
    this.lastAccesseOn = lastAccesseOn;
  }
  public AccessStatus firstAccesseOn(Long firstAccesseOn) {
    this.firstAccesseOn = firstAccesseOn;
    return this;
  }

  

  /**
  * Get firstAccesseOn
  * @return firstAccesseOn
  **/
  @Schema(description = "")
  public Long getFirstAccesseOn() {
    return firstAccesseOn;
  }
  public void setFirstAccesseOn(Long firstAccesseOn) {
    this.firstAccesseOn = firstAccesseOn;
  }
  public AccessStatus onlineTimeInSec(Float onlineTimeInSec) {
    this.onlineTimeInSec = onlineTimeInSec;
    return this;
  }

  

  /**
  * Get onlineTimeInSec
  * @return onlineTimeInSec
  **/
  @Schema(description = "")
  public Float getOnlineTimeInSec() {
    return onlineTimeInSec;
  }
  public void setOnlineTimeInSec(Float onlineTimeInSec) {
    this.onlineTimeInSec = onlineTimeInSec;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AccessStatus accessStatus = (AccessStatus) o;
    return Objects.equals(this.createdOn, accessStatus.createdOn) &&
        Objects.equals(this.lastAccesseOn, accessStatus.lastAccesseOn) &&
        Objects.equals(this.firstAccesseOn, accessStatus.firstAccesseOn) &&
        Objects.equals(this.onlineTimeInSec, accessStatus.onlineTimeInSec);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(createdOn, lastAccesseOn, firstAccesseOn, onlineTimeInSec);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AccessStatus {\n");
    
    sb.append("    createdOn: ").append(toIndentedString(createdOn)).append("\n");
    sb.append("    lastAccesseOn: ").append(toIndentedString(lastAccesseOn)).append("\n");
    sb.append("    firstAccesseOn: ").append(toIndentedString(firstAccesseOn)).append("\n");
    sb.append("    onlineTimeInSec: ").append(toIndentedString(onlineTimeInSec)).append("\n");
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
