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
 * FaceAttributes
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2018-12-06T15:12:58.891Z[GMT]")public class FaceAttributes {

  @SerializedName("smile")
  private Float smile = null;
  /**
   * Gets or Sets gender
   */
  @JsonAdapter(GenderEnum.Adapter.class)
  public enum GenderEnum {
    MALE("male"),
    FEMALE("female"),
    NONE("none");

    private String value;

    GenderEnum(String value) {
      this.value = value;
    }
    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }
    public static GenderEnum fromValue(String text) {
      for (GenderEnum b : GenderEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }
    public static class Adapter extends TypeAdapter<GenderEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final GenderEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public GenderEnum read(final JsonReader jsonReader) throws IOException {
        String value = jsonReader.nextString();
        return GenderEnum.fromValue(String.valueOf(value));
      }
    }
  }
  @SerializedName("gender")
  private GenderEnum gender = null;

  @SerializedName("age")
  private Float age = null;
  /**
   * Gets or Sets glasses
   */
  @JsonAdapter(GlassesEnum.Adapter.class)
  public enum GlassesEnum {
    GLASSES("glasses"),
    NOGALSSES("noGalsses");

    private String value;

    GlassesEnum(String value) {
      this.value = value;
    }
    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }
    public static GlassesEnum fromValue(String text) {
      for (GlassesEnum b : GlassesEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }
    public static class Adapter extends TypeAdapter<GlassesEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final GlassesEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public GlassesEnum read(final JsonReader jsonReader) throws IOException {
        String value = jsonReader.nextString();
        return GlassesEnum.fromValue(String.valueOf(value));
      }
    }
  }
  @SerializedName("glasses")
  private GlassesEnum glasses = null;
  public FaceAttributes smile(Float smile) {
    this.smile = smile;
    return this;
  }

  

  /**
  * Get smile
  * @return smile
  **/
  @Schema(example = "0.562", description = "")
  public Float getSmile() {
    return smile;
  }
  public void setSmile(Float smile) {
    this.smile = smile;
  }
  public FaceAttributes gender(GenderEnum gender) {
    this.gender = gender;
    return this;
  }

  

  /**
  * Get gender
  * @return gender
  **/
  @Schema(example = "female", description = "")
  public GenderEnum getGender() {
    return gender;
  }
  public void setGender(GenderEnum gender) {
    this.gender = gender;
  }
  public FaceAttributes age(Float age) {
    this.age = age;
    return this;
  }

  

  /**
  * Get age
  * @return age
  **/
  @Schema(example = "22.9", description = "")
  public Float getAge() {
    return age;
  }
  public void setAge(Float age) {
    this.age = age;
  }
  public FaceAttributes glasses(GlassesEnum glasses) {
    this.glasses = glasses;
    return this;
  }

  

  /**
  * Get glasses
  * @return glasses
  **/
  @Schema(description = "")
  public GlassesEnum getGlasses() {
    return glasses;
  }
  public void setGlasses(GlassesEnum glasses) {
    this.glasses = glasses;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FaceAttributes faceAttributes = (FaceAttributes) o;
    return Objects.equals(this.smile, faceAttributes.smile) &&
        Objects.equals(this.gender, faceAttributes.gender) &&
        Objects.equals(this.age, faceAttributes.age) &&
        Objects.equals(this.glasses, faceAttributes.glasses);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(smile, gender, age, glasses);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FaceAttributes {\n");
    
    sb.append("    smile: ").append(toIndentedString(smile)).append("\n");
    sb.append("    gender: ").append(toIndentedString(gender)).append("\n");
    sb.append("    age: ").append(toIndentedString(age)).append("\n");
    sb.append("    glasses: ").append(toIndentedString(glasses)).append("\n");
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
