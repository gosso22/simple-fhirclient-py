import fhirclient.models.coding as coding
import fhirclient.models.codeableconcept as cc

location_coding = coding.Coding()
location_coding.system = 'http://terminology.hl7.org/CodeSystem/location-physical-type'
location_coding.code = 'jnd'
location_coding.display = 'Jurisdiction'

catchment_codeable_concept = cc.CodeableConcept()
catchment_codeable_concept.coding = [location_coding]
