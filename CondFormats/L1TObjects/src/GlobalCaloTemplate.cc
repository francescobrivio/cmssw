/**
 * \class GlobalCaloTemplate
 *
 *
 * Description: L1 Global Trigger calo template.
 *
 * Implementation:
 *    <TODO: enter implementation details>
 *
 * \author: Vasile Mihai Ghete - HEPHY Vienna
 *
 * $Date$
 * $Revision$
 *
 */

// this class header
#include "CondFormats/L1TObjects/interface/GlobalCaloTemplate.h"

// system include files

#include <iostream>
#include <iomanip>

// user include files

//   base class

#include "CondFormats/L1TObjects/interface/L1GtFwd.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutSetupFwd.h"

// forward declarations

// constructors
GlobalCaloTemplate::GlobalCaloTemplate()
        : GlobalCondition()
{

    m_condCategory = l1t::CondCalo;

}

GlobalCaloTemplate::GlobalCaloTemplate(const std::string& cName)
        : GlobalCondition(cName)
{

    m_condCategory = l1t::CondCalo;

}

GlobalCaloTemplate::GlobalCaloTemplate(const std::string& cName, const l1t::GlobalConditionType& cType)
        : GlobalCondition(cName, l1t::CondCalo, cType)
{

    int nObjects = nrObjects();

    if (nObjects > 0) {
        m_objectParameter.reserve(nObjects);

        m_objectType.reserve(nObjects);
    }

}

// copy constructor
GlobalCaloTemplate::GlobalCaloTemplate(const GlobalCaloTemplate& cp)
        : GlobalCondition(cp.m_condName)
{
    copy(cp);
}

// destructor
GlobalCaloTemplate::~GlobalCaloTemplate()
{
    // empty now
}

// assign operator
GlobalCaloTemplate& GlobalCaloTemplate::operator= (const GlobalCaloTemplate& cp)
{

    copy(cp);
    return *this;
}


// setConditionParameter - set the parameters of the condition
void GlobalCaloTemplate::setConditionParameter(
    const std::vector<ObjectParameter>& objParameter,
    const CorrelationParameter& corrParameter)
{

    m_objectParameter = objParameter;
    m_correlationParameter = corrParameter;

}

void GlobalCaloTemplate::print(std::ostream& myCout) const
{

    myCout << "\n  GlobalCaloTemplate print..." << std::endl;

    GlobalCondition::print(myCout);

    int nObjects = nrObjects();

    for (int i = 0; i < nObjects; i++) {
        myCout << std::endl;
        myCout << "  Template for object " << i << " [ hex ]" << std::endl;
        myCout << "    etThreshold       = "
        << std::hex << m_objectParameter[i].etThreshold << std::endl;
        myCout << "    etaRange          = "
        << std::hex << m_objectParameter[i].etaRange << std::endl;
        myCout << "    phiRange          = "
        << std::hex << m_objectParameter[i].phiRange << std::endl;
    }

    if ( wsc() ) {

        myCout << "  Correlation parameters " << "[ hex ]" <<  std::endl;

        myCout << "    deltaEtaRange     = "
        << std::hex << m_correlationParameter.deltaEtaRange << std::endl;
        myCout << "    deltaPhiRange     = "
        << std::hex << m_correlationParameter.deltaPhiRange << std::endl;
        myCout << "    deltaPhiMaxbits   = "
        << std::hex << m_correlationParameter.deltaPhiMaxbits << std::endl;
    }

    // reset to decimal output
    myCout << std::dec << std::endl;
}

void GlobalCaloTemplate::copy(const GlobalCaloTemplate& cp)
{

    m_condName     = cp.condName();
    m_condCategory = cp.condCategory();
    m_condType     = cp.condType();
    m_objectType   = cp.objectType();
    m_condGEq      = cp.condGEq();
    m_condChipNr   = cp.condChipNr();
    m_condRelativeBx = cp.condRelativeBx();

    m_objectParameter = *(cp.objectParameter());
    m_correlationParameter = *(cp.correlationParameter());

}

// output stream operator
std::ostream& operator<<(std::ostream& os, const GlobalCaloTemplate& result)
{
    result.print(os);
    return os;

}



