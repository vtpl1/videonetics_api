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
import io.swagger.client.model.AccessStatus;
import io.swagger.client.model.Enterprise;
import io.swagger.client.model.EnterpriseAccountStatus;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
import java.util.UUID;

/**
 * EnterpriseDetail
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2018-12-06T15:15:06.313Z[GMT]")public class EnterpriseDetail extends AccessStatus {

  @SerializedName("id")
  private UUID id = null;

  @SerializedName("name")
  private String name = null;

  @SerializedName("logo")
  private String logo = null;

  @SerializedName("address")
  private String address = null;

  @SerializedName("contact")
  private String contact = null;

  @SerializedName("accountStatus")
  private EnterpriseAccountStatus accountStatus = null;
  public EnterpriseDetail id(UUID id) {
    this.id = id;
    return this;
  }

  

  /**
  * Get id
  * @return id
  **/
  @Schema(required = true, description = "")
  public UUID getId() {
    return id;
  }
  public void setId(UUID id) {
    this.id = id;
  }
  public EnterpriseDetail name(String name) {
    this.name = name;
    return this;
  }

  

  /**
  * Get name
  * @return name
  **/
  @Schema(required = true, description = "")
  public String getName() {
    return name;
  }
  public void setName(String name) {
    this.name = name;
  }
  public EnterpriseDetail logo(String logo) {
    this.logo = logo;
    return this;
  }

  

  /**
  * Get logo
  * @return logo
  **/
  @Schema(description = "")
  public String getLogo() {
    return logo;
  }
  public void setLogo(String logo) {
    this.logo = logo;
  }
  public EnterpriseDetail address(String address) {
    this.address = address;
    return this;
  }

  

  /**
  * Get address
  * @return address
  **/
  @Schema(description = "")
  public String getAddress() {
    return address;
  }
  public void setAddress(String address) {
    this.address = address;
  }
  public EnterpriseDetail contact(String contact) {
    this.contact = contact;
    return this;
  }

  

  /**
  * Get contact
  * @return contact
  **/
  @Schema(description = "")
  public String getContact() {
    return contact;
  }
  public void setContact(String contact) {
    this.contact = contact;
  }
  public EnterpriseDetail accountStatus(EnterpriseAccountStatus accountStatus) {
    this.accountStatus = accountStatus;
    return this;
  }

  

  /**
  * Get accountStatus
  * @return accountStatus
  **/
  @Schema(required = true, description = "")
  public EnterpriseAccountStatus getAccountStatus() {
    return accountStatus;
  }
  public void setAccountStatus(EnterpriseAccountStatus accountStatus) {
    this.accountStatus = accountStatus;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EnterpriseDetail enterpriseDetail = (EnterpriseDetail) o;
    return Objects.equals(this.id, enterpriseDetail.id) &&
        Objects.equals(this.name, enterpriseDetail.name) &&
        Objects.equals(this.logo, enterpriseDetail.logo) &&
        Objects.equals(this.address, enterpriseDetail.address) &&
        Objects.equals(this.contact, enterpriseDetail.contact) &&
        Objects.equals(this.accountStatus, enterpriseDetail.accountStatus) &&
        super.equals(o);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(id, name, logo, address, contact, accountStatus, super.hashCode());
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class EnterpriseDetail {\n");
    sb.append("    ").append(toIndentedString(super.toString())).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    logo: ").append(toIndentedString(logo)).append("\n");
    sb.append("    address: ").append(toIndentedString(address)).append("\n");
    sb.append("    contact: ").append(toIndentedString(contact)).append("\n");
    sb.append("    accountStatus: ").append(toIndentedString(accountStatus)).append("\n");
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
