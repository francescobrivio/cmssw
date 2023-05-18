import FWCore.ParameterSet.Config as cms
process = cms.Process("GeometryInfo")

# minimum of logs
process.MessageLogger = cms.Service("MessageLogger",
    cerr = cms.untracked.PSet(
        enable = cms.untracked.bool(False)
    ),
    cout = cms.untracked.PSet(
        enable = cms.untracked.bool(True),
        threshold = cms.untracked.string('INFO')
    )
)

# input/output databases (in this case local sqlite files)
process.load("CondCore.CondDB.CondDB_cfi")
#process.CondDB.connect = 'sqlite_file:PPS_RecoGeometry_test_v1.db'
process.CondDB.connect = 'frontier://FrontierPrep/CMS_CONDITIONS'
process.PoolDBESSource = cms.ESSource("PoolDBESSource",
    process.CondDB,
    DumpStat=cms.untracked.bool(False), #True
    toGet = cms.VPSet(
      cms.PSet(
        record = cms.string('VeryForwardIdealGeometryRecord'),
        tag = cms.string("PPS_RecoGeometry_test_v1")
      )
    )
)

process.newCondDB = process.CondDB.clone()
process.newCondDB.connect = 'sqlite_file:dataout.db'
process.PoolDBOutputService = cms.Service("PoolDBOutputService",
    process.newCondDB,
    timetype = cms.untracked.string('runnumber'),
    toPut = cms.VPSet(cms.PSet(
        record = cms.string('VeryForwardIdealGeometryRecord'),
        tag = cms.string('PPSGeometry_test')
    ))
)

# geometry
process.ctppsGeometryESModule = cms.ESProducer("CTPPSGeometryESModule",
    fromPreprocessedDB = cms.untracked.bool(True),
    fromDD4hep = cms.untracked.bool(False),
    verbosity = cms.untracked.uint32(1),
)


# load alignment correction
process.load("CalibPPS.ESProducers.ctppsRPAlignmentCorrectionsDataESSourceXML_cfi")
process.ctppsRPAlignmentCorrectionsDataESSourceXML.RealFiles = cms.vstring(
    "Geometry/VeryForwardGeometryBuilder/test/alignment_file_1.xml",
    "Geometry/VeryForwardGeometryBuilder/test/alignment_file_2.xml",
)
process.ctppsRPAlignmentCorrectionsDataESSourceXML.verbosity = 1

# no events to process
process.source = cms.Source("EmptySource",
#  firstRun = cms.untracked.uint32(273725),  # start run for 2016-2017
  firstRun = cms.untracked.uint32(314747),  # start run for 2018
  firstLuminosityBlock = cms.untracked.uint32(1),
  firstEvent = cms.untracked.uint32(1),
  numberEventsInLuminosityBlock = cms.untracked.uint32(3),
  numberEventsInRun = cms.untracked.uint32(30)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

process.ctppsGeometryInfo = cms.EDAnalyzer("CTPPSGeometryInfo",
    geometryType = cms.untracked.string("real"),
    printRPInfo = cms.untracked.bool(True),
    printSensorInfo = cms.untracked.bool(True)
)

process.p = cms.Path(
    process.ctppsGeometryInfo
)
