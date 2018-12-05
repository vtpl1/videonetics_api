package io.swagger.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import org.springframework.validation.annotation.Validated;
import javax.validation.Valid;
import javax.validation.constraints.*;

/**
 * FaceAttributes
 */
@Validated
@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2018-12-05T09:37:54.774Z[GMT]")

public class FaceAttributes   {
  @JsonProperty("smile")
  private Float smile = null;

  /**
   * Gets or Sets gender
   */
  public enum GenderEnum {
    MALE("male"),
    
    FEMALE("female"),
    
    NONE("none");

    private String value;

    GenderEnum(String value) {
      this.value = value;
    }

    @Override
    @JsonValue
    public String toString() {
      return String.valueOf(value);
    }

    @JsonCreator
    public static GenderEnum fromValue(String text) {
      for (GenderEnum b : GenderEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }
  }

  @JsonProperty("gender")
  private GenderEnum gender = null;

  @JsonProperty("age")
  private Float age = null;

  /**
   * Gets or Sets glasses
   */
  public enum GlassesEnum {
    GLASSES("glasses"),
    
    NOGALSSES("noGalsses");

    private String value;

    GlassesEnum(String value) {
      this.value = value;
    }

    @Override
    @JsonValue
    public String toString() {
      return String.valueOf(value);
    }

    @JsonCreator
    public static GlassesEnum fromValue(String text) {
      for (GlassesEnum b : GlassesEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }
  }

  @JsonProperty("glasses")
  private GlassesEnum glasses = null;

  public FaceAttributes smile(Float smile) {
    this.smile = smile;
    return this;
  }

  /**
   * Get smile
   * @return smile
  **/
  @ApiModelProperty(example = "0.562", value = "")


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
  @ApiModelProperty(example = "female", value = "")


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
  @ApiModelProperty(example = "22.9", value = "")


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
  @ApiModelProperty(value = "")


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
    return Objects.hash(smile, gender, age, glasses);
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

