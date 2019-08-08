/* Copyright (c) 2017 Boundless - http://boundlessgeo.com All rights reserved.
 * This code is licensed under the GPL 2.0 license, available at the root
 * application directory.
 */
package com.boundlessgeo.gsr.api.feature;

import java.io.IOException;
import java.util.Arrays;
import java.util.Collections;
import java.util.NoSuchElementException;

import com.boundlessgeo.gsr.model.geometry.SpatialReference;
import com.boundlessgeo.gsr.translate.geometry.SpatialReferenceEncoder;
import com.boundlessgeo.gsr.translate.geometry.SpatialReferences;
import com.boundlessgeo.gsr.translate.map.LayerDAO;
import org.geoserver.api.APIService;
import org.geoserver.api.HTMLResponseBody;
import org.geoserver.api.styles.StylesServiceInfo;
import org.geoserver.catalog.FeatureTypeInfo;
import org.geoserver.config.GeoServer;
import org.geoserver.wfs.WFSInfo;
import org.geotools.data.FeatureSource;
import org.geotools.feature.FeatureCollection;
import org.opengis.filter.Filter;
import org.opengis.referencing.FactoryException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.boundlessgeo.gsr.api.AbstractGSRController;
import com.boundlessgeo.gsr.translate.feature.FeatureEncoder;
import com.boundlessgeo.gsr.model.AbstractGSRModel.Link;
import com.boundlessgeo.gsr.model.feature.FeatureWrapper;
import com.boundlessgeo.gsr.model.map.LayerOrTable;

/**
 * Controller for the Feature Service feature list endpoint
 */
@APIService(
        service = "Feature",
        version = "1.0",
        landingPage = "/gsr/services",
        serviceClass = WFSInfo.class
)
@RestController
@RequestMapping(path = "/gsr/services/{workspaceName}/FeatureServer", produces = MediaType.APPLICATION_JSON_VALUE)
public class FeatureController extends AbstractGSRController {

    @Autowired
    public FeatureController(@Qualifier("geoServer") GeoServer geoServer) {
        super(geoServer);
    }

    @GetMapping(path = "/{layerId}/{featureId}")
    @HTMLResponseBody(templateName = "featureitem.ftl", fileName = "featureitem.html")
    public FeatureWrapper featureGet(@PathVariable String workspaceName, @PathVariable Integer layerId, @PathVariable String featureId) throws IOException, FactoryException {
        LayerOrTable l = LayerDAO.find(catalog, workspaceName, layerId, Collections.emptyList(), Collections.emptyList());

        if (null == l) {
            throw new NoSuchElementException("No table or layer in workspace \"" + workspaceName + "\" for id " + layerId);
        }

        FeatureTypeInfo featureType = (FeatureTypeInfo) l.layer.getResource();
        if (null == featureType) {
            throw new NoSuchElementException("No table or layer in workspace \"" + workspaceName + "\" for id " + layerId);
        }


        Filter idFilter = FILTERS.id(FILTERS.featureId(featureType.getFeatureType().getName().getLocalPart() + "." + featureId));

        FeatureSource<?, ?> source = featureType.getFeatureSource(null, null);
        FeatureCollection<?, ?> featureColl = source.getFeatures(idFilter);
        org.opengis.feature.Feature[] featureArr = featureColl.toArray(new org.opengis.feature.Feature[0]);
        if (featureArr.length == 0) {
            throw new NoSuchElementException("No feature in layer or table " + layerId + " with id " + featureId);
        }
        SpatialReference spatialReference = SpatialReferences.fromCRS(featureArr[0].getDefaultGeometryProperty().getDescriptor().getCoordinateReferenceSystem());
        return new FeatureWrapper(FeatureEncoder.feature(featureArr[0], true, spatialReference), Arrays.asList(
                new Link(workspaceName, workspaceName),
                new Link(workspaceName + "/" + "FeatureServer", "FeatureServer"),
                new Link(workspaceName + "/" + "FeatureServer/" + layerId, l.getName()),
                new Link(workspaceName + "/" + "FeatureServer/" + layerId + "/" + featureId, featureId)),
                Collections.singletonList(new Link(workspaceName + "/" + "FeatureServer/" + layerId + "/" + featureId + "?f=json&pretty=true", "REST")));
    }
}
